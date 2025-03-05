return {
	{
		"lukas-reineke/indent-blankline.nvim",
		main = "ibl", -- Ensures we use the latest 'ibl' module
		event = { "BufReadPost", "BufNewFile" },
		opts = {
			scope = {
				enabled = true,
				show_start = false, -- Hide start indicators
				show_end = false, -- Hide end indicators
			},
			exclude = {
				filetypes = {
					"help",
					"dashboard",
					"lazy",
					"mason",
					"neo-tree",
					"Trouble",
					"alpha",
				},
			},
		},
		config = function(_, opts)
			require("ibl").setup(opts)
		end,
	},
}
