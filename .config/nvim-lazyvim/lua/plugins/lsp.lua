-- File: ~/.config/nvim/lua/plugins/lsp.lua
-- Example LazyNeovim configuration that:
-- 1. Detects if the user has previously selected a Conda environment for this project.
-- 2. If not, lists all Conda environments, prompts the user to pick one, and saves that choice.
-- 3. Uses the chosen environment's Python interpreter for Pyright in that project.

local lspconfig = require("lspconfig")

-- Helper: Return a table of {name, path} for each Conda environment
local function list_conda_envs()
  local envs = {}
  -- Attempt to grab environment info via `conda env list`.
  -- (Make sure `conda` is in your PATH.)
  local output = vim.fn.systemlist("conda env list")

  -- Typical lines look like:
  -- base                  *  /home/user/anaconda3
  -- my_env                  /home/user/anaconda3/envs/my_env
  --
  -- We'll parse each line by splitting on spaces.
  for _, line in ipairs(output) do
    if not line:match("^#") and line:match("%S") then
      -- Remove any "*" markers
      local clean_line = line:gsub("%*", ""):gsub("%s+", " ")
      -- Split into fields
      local fields = {}
      for field in clean_line:gmatch("%S+") do
        table.insert(fields, field)
      end
      -- Usually, fields[1] = env_name, fields[#fields] = path
      -- (Edge cases can happen, but typically the env name is first or blank for 'base' environment.)
      if #fields >= 2 then
        local path = fields[#fields]
        local name = table.concat(fields, " ", 1, #fields - 1)
        -- Trim leading/trailing spaces
        name = name:gsub("^%s+", ""):gsub("%s+$", "")
        table.insert(envs, { name = name, path = path })
      end
    end
  end
  return envs
end

-- Helper: Ask user which Conda env to use (if multiple).
-- Returns the env path or nil if none chosen/cancelled.
local function pick_conda_env(envs)
  if #envs == 0 then
    return nil
  end

  -- Prepare a list for inputlist
  local choices = { "Select a Conda environment for this project:" }
  for i, env in ipairs(envs) do
    table.insert(choices, string.format("%d) %s (%s)", i, env.name, env.path))
  end

  local choice = vim.fn.inputlist(choices) -- Blocks for user input
  if choice < 1 or choice > #envs then
    return nil
  end

  return envs[choice].path
end

-- This function checks if there's a saved Conda env for the project.
-- If not, it prompts the user, then saves it in .conda_env_selected (per project).
local function resolve_conda_env(root_dir)
  local conda_file = root_dir .. "/.conda_env_selected"
  -- 1) If a file with the chosen env path already exists, read it and return
  if vim.fn.filereadable(conda_file) == 1 then
    local lines = vim.fn.readfile(conda_file)
    if lines and #lines > 0 then
      return lines[1] -- the saved path
    end
  end

  -- 2) If no saved env, we gather conda envs and ask the user
  local envs = list_conda_envs()
  local chosen_path = pick_conda_env(envs)
  if chosen_path then
    -- Save the chosen path to the file so we don't ask again
    vim.fn.writefile({ chosen_path }, conda_file)
    return chosen_path
  end

  return nil
end

-- Helper: Construct a python path from the chosen env path (supports Windows vs. others).
local function get_python_from_conda_env(env_path)
  if vim.fn.has("win32") == 1 or vim.fn.has("win64") == 1 then
    return env_path .. "\\python.exe"
  else
    return env_path .. "/bin/python"
  end
end

-- Finally, set up Pyright using the above logic:
local function pyright_with_conda()
  return {
    before_init = function(_, config)
      local root_dir = config.root_dir or vim.fn.getcwd()
      local conda_env_path = resolve_conda_env(root_dir)
      if conda_env_path and vim.fn.isdirectory(conda_env_path) == 1 then
        config.settings.python.pythonPath = get_python_from_conda_env(conda_env_path)
      else
        -- Fallback: system python if no Conda env selected
        config.settings.python.pythonPath = "python"
      end
    end,
    settings = {
      python = {
        analysis = {
          autoSearchPaths = true,
          diagnosticMode = "workspace",
          useLibraryCodeForTypes = true,
        },
      },
    },
  }
end

-- Return the LazyVim plugin specification
return {
  {
    "williamboman/mason.nvim",
    build = ":MasonUpdate",
  },
  {
    "williamboman/mason-lspconfig.nvim",
    opts = {
      ensure_installed = { "pyright" },
    },
  },
  {
    "neovim/nvim-lspconfig",
    dependencies = {
      "williamboman/mason.nvim",
      "williamboman/mason-lspconfig.nvim",
    },
    opts = {
      servers = {
        -- Attach our custom config for Pyright
        pyright = pyright_with_conda(),
      },
    },
  },
}
