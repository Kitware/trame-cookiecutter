export default {
  base: "./",
  build: {
    lib: {
      entry: "./src/main.js",
      name: "{{cookiecutter.import_name}}",
      formats: ["umd"],
      fileName: "{{cookiecutter.import_name}}",
    },
    rollupOptions: {
      external: ["vue"],
      output: {
        globals: {
          vue: "Vue",
        },
      },
    },
    outDir: "../src/{{cookiecutter.import_name}}/module/serve",
    assetsDir: ".",
  },
};
