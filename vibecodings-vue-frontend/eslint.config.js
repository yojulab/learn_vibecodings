import globals from "globals";
import pluginVue from "eslint-plugin-vue";
import tsEslint from "typescript-eslint";
import prettierConfig from "eslint-config-prettier";

export default [
  {
    files: ["**/*.{js,mjs,cjs,ts,vue}"],
    languageOptions: {
      globals: {
        ...globals.browser,
        ...globals.node,
      },
      parser: "vue-eslint-parser",
      parserOptions: {
        parser: tsEslint.parser,
        sourceType: "module",
        ecmaVersion: "latest",
        extraFileExtensions: [".vue"],
      },
    },
    plugins: {
      vue: pluginVue,
    },
    rules: {
      ...pluginVue.configs["vue3-essential"].rules,
      ...pluginVue.configs["vue3-strongly-recommended"].rules,
      ...pluginVue.configs["vue3-recommended"].rules,
      // Add custom rules here if needed
    },
  },
  ...tsEslint.configs.recommended,
  prettierConfig,
];
