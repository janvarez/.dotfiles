return {}
--   {
--     "williamboman/mason.nvim",
-- 	opts = {},
--   },
--   {
--     "williamboman/mason-lspconfig.nvim",
--     lazy = false,
--     opts = {
--         ensure_installed = {"bashls","ts_ls","ruff","cmake","tailwindcss","dockerls"}}
--   },
--   {
--     "neovim/nvim-lspconfig",
--     config = function()
--       local capabilities = require('cmp_nvim_lsp').default_capabilities()
--       local lspconfig = require("lspconfig")
--
--       lspconfig.ruff.setup({ capabilities = capabilities })
--       lspconfig.lua_ls.setup({ capabilities = capabilities })
--       lspconfig.ts_ls.setup({ capabilities = capabilities })
--       lspconfig.bashls.setup({ capabilities = capabilities })
--       lspconfig.tailwindcss.setup({ capabilities = capabilities })
--       lspconfig.dockerls.setup({ capabilities = capabilities })
--
--       vim.keymap.set('n', 'K', vim.lsp.buf.hover, {})
--       vim.keymap.set('n', '<leader>gd', vim.lsp.buf.definition, {})
--       vim.keymap.set('n', '<leader>gr', vim.lsp.buf.references, {})
--       vim.keymap.set({ 'n', 'v' }, '<leader>ca', vim.lsp.buf.code_action, {})
--
--       vim.keymap.set('n', '<leader>gD', vim.lsp.buf.declaration, {})
--       vim.keymap.set('n', '<leader>gi', vim.lsp.buf.implementation, {})
--       vim.keymap.set('n', '<leader>go', vim.lsp.buf.type_definition, {})
--       vim.keymap.set('n', '<leader>gs', vim.lsp.buf.signature_help, {})
--       vim.keymap.set('n', '<F2>', vim.lsp.buf.rename, {})
--     end
--   }
-- }
