<template>
  <v-container>
    <v-row>
      <Date />
    </v-row>
    <v-row>
      <v-col cols="3">
        <Table />
      </v-col>
      <v-col cols="9">
        <Graph />
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
import Date from "./Date";
import Table from "./Table";
import Graph from "./Graph";
export default {
  name: "Monitor",

  components: {
    Date,
    Table,
    Graph
  }
};
</script>
<style lang="stylus" scoped></style>