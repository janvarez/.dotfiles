vim.g.mapleader = " "
vim.g.maplocalleader = " "

local opts = { noremap = true, silent = true }

vim.keymap.set("n", "<C-n>", ":Neotree toggle filesystem left<CR>", opts)

vim.keymap.set("n", "<C-k>", ":wincmd k<CR>")
vim.keymap.set("n", "<C-j>", ":wincmd j<CR>")
vim.keymap.set("n", "<C-h>", ":wincmd h<CR>")
vim.keymap.set("n", "<C-l>", ":wincmd l<CR>")

-- clear highlights
vim.keymap.set("n", "<Esc>", ":noh<CR>", opts)

-- save file
vim.keymap.set("n", "<C-S>", "<cmd> w <CR>", opts)

-- save file without auto-formatting
vim.keymap.set("n", "<leader>sn", "<cmd>noautocmd w <CR>", { desc = "[S]ave [N]ormal" })

-- quit file
vim.keymap.set("n", "<leader>fq", "<cmd> q <CR>", { desc = "[F]ile [Q]uit" })

-- Quit Neovim
vim.keymap.set("n", "<leader>qq", "<cmd> wqa <CR>", { desc = "[Q]uit [Q]uit" })

-- Move text up and down
vim.keymap.set("v", "<A-k>", ":m .-2<CR>==", opts)
vim.keymap.set("v", "<A-j>", ":m .+1<CR>==", opts)

-- Replace word under cursor
vim.keymap.set("n", "<leader>j", "*``cgn", { desc = "Replace under cursor", noremap = true, silent = true })

-- delete single character without copying into register
vim.keymap.set("n", "x", '"_x', { desc = "Delete single character" })

-- Toggle line wrapping
vim.keymap.set("n", "<leader>lw", "<cmd>set wrap!<CR>", { desc = "[L]ine [W]rapping Toggle" })

-- Stay in indent mode
vim.keymap.set("v", "<", "<gv", opts)
vim.keymap.set("v", ">", ">gv", opts)

-- Explicitly yank to system clipboard (highlighted and entire row)
vim.keymap.set({ "n", "v" }, "<leader>y", [["+y]], { desc = "[Y]ank highlighted" })
vim.keymap.set("n", "<leader>Y", [["+Y]], { desc = "[Y]ank Row" })

vim.keymap.set({ "n", "v" }, "<Space>", "<Nop>", { silent = true })

-- Toggle diagnostics
local diagnostics_active = true

vim.keymap.set("n", "<leader>dt", function()
	diagnostics_active = not diagnostics_active

	if diagnostics_active then
		vim.diagnostic.enable(true)
	else
		vim.diagnostic.enable(false)
	end
end, { desc = "[D]iagnostics [T]oggle" })

-- Diagnostic keymaps
vim.keymap.set("n", "[d", vim.diagnostic.goto_prev, { desc = "Go to previous diagnostic message" })
vim.keymap.set("n", "]d", vim.diagnostic.goto_next, { desc = "Go to next diagnostic message" })
vim.keymap.set("n", "<leader>df", vim.diagnostic.open_float, { desc = "[D]iagnostic [M]essage inspect" })
vim.keymap.set("n", "<leader>dl", vim.diagnostic.setloclist, { desc = "[D]iagnostics [L]ist" })

vim.keymap.set("n", "L", ":BufferLineCycleNext<CR>", { silent = true })
vim.keymap.set("n", "H", ":BufferLineCyclePrev<CR>", { silent = true })
-- vim.keymap.set("n", "<leader>D", ":bdelete!<CR>", { silent = true })
-- Keymaps are automatically loaded on the VeryLazy event
-- Default keymaps that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/keymaps.lua
-- Add any additional keymaps her
--

-- Save and load session
vim.keymap.set(
	"n",
	"<leader>ss",
	":mksession! .session.vim<CR>",
	{ desc = "[S]ession [S]ave", noremap = true, silent = false }
)
vim.keymap.set(
	"n",
	"<leader>sl",
	":source .session.vim<CR>",
	{ desc = "[S]ession [L]oad", noremap = true, silent = false }
)

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
