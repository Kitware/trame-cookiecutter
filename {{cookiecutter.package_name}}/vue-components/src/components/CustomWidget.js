export default {
    emits: ["click", "change"],
    props: {
      attribute_name: {
        type: String,
      },
      js_attr_name: {
        type: String,
      },
    },
    setup(props, { emit }) {
        const btnClick = "margin: 0 10px;background: #F48FB1 !important;";
        const btnChange = "margin: 0 10px;#CE93D8 !important;";
        const triggerClick = () => emit("click");
        const triggerChange = () => emit("change");

        return {
          btnClick, 
          btnChange, 
          triggerClick, 
          triggerChange,
        };
    },
    template: `
        <div>
            <v-btn @click="triggerClick" :style="btnClick">Custom click</v-btn>
            <v-btn @click="triggerChange" :style="btnChange">Custom change</v-btn>
        </div>`,
  };
  