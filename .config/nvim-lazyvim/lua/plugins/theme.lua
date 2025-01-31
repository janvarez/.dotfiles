-- lua/plugins/catppuccin.lua
return {
  "catppuccin/nvim",
  name = "catppuccin",
  lazy = false, -- or true, depending on your preference
  priority = 1000, -- ensure it loads first
  config = function()
    require("catppuccin").setup({
      flavour = "mocha", -- or latte, macchiato, frappe
      transparent_background = false,
      integrations = {
        cmp = true,
        treesitter = true,
        telescope = true,
        neotree = true, -- enable/disable other plugins here
      },
    })
    vim.cmd.colorscheme("catppuccin")
  end,
}
