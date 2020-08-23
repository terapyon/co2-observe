<template>
  <v-data-table
    :headers="headers"
    :items="desserts"
    :sort-by="['time']"
    :sort-desc="[false]"
    multi-sort
    class="elevation-1"
  ></v-data-table>
</template>
<script>
export default {
  name: "Table",

  components: {},

  data() {
    return {
      headers: [
        {
          text: "5分おきデータ",
          align: "start",
          sortable: true,
          value: "time"
        },
        { text: "CO2(ppm)", value: "co2" },
        { text: "温度(℃)", value: "temperature" }
      ]
    };
  },
  computed: {
    desserts() {
      return this.$store.state.timeData;
    }
  }
};
</script>
<style lang="stylus" scoped></style>