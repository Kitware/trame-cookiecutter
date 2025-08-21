import "./style.css";

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
    const triggerClick = () => emit("click");
    const triggerChange = () => emit("change");

    return {
      triggerClick,
      triggerChange,
    };
  },
  template: `
        <div>
            <v-btn @click="triggerClick" class="btnClick">Custom click</v-btn>
            <v-btn @click="triggerChange" class="btnChange">Custom change</v-btn>
        </div>`,
};
