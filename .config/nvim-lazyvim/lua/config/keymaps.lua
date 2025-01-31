-- Keymaps are automatically loaded on the VeryLazy event
-- Default keymaps that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/keymaps.lua
-- Add any additional keymaps her
--
vim.keymap.set("n", "<leader>r", function()
  -- 1. Save the current file
  vim.cmd("write")

  -- 2. Open a horizontal split at the bottom, 10 lines high, in the *same* tab
  -- Use 'botright 10split' so it doesn't replace your code window and stays in the same tab
  vim.cmd("botright 10split")

  -- 3. Launch a terminal in that new split, running the current file via Python
  -- Adjust 'python' vs 'python3' if needed
  vim.cmd("terminal python " .. vim.fn.expand("%"))

  -- 4. If you prefer to stay in the terminal, remove the next line;
  --    if you want to jump back to your code window, keep it.
  vim.cmd("wincmd p") -- Jump back to previous window (the code)
end, { desc = "Run current Python file in bottom split terminal" })
-- This file is automatically loaded by lazyvim.config.init
