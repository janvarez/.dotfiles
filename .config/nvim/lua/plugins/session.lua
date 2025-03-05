return {
	"shatur/neovim-session-manager",
	config = function()
		-- Import session_manager and its config
		local session_manager = require("session_manager")
		local config = require("session_manager.config")

		-- Set autoload mode
		session_manager.setup({
			autoload_mode = config.AutoloadMode.CurrentDir,
		})

		-- Create an autocommand group
		local config_group = vim.api.nvim_create_augroup("MyConfigGroup", {})

		-- Automatically toggle neo-tree after loading a session
		vim.api.nvim_create_autocmd("User", {
			pattern = "SessionLoadPost",
			group = config_group,
			callback = function()
				vim.cmd("Neotree toggle")
			end,
		})

		-- Auto-save session before writing any buffer, unless a 'nofile' buffer is open
		vim.api.nvim_create_autocmd("BufWritePre", {
			callback = function()
				for _, buf in ipairs(vim.api.nvim_list_bufs()) do
					if vim.api.nvim_get_option_value("buftype", { buf = buf }) == "nofile" then
						return
					end
				end
				session_manager.save_current_session()
			end,
		})
	end,
}
