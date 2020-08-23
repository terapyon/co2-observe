<template>
  <v-row>
    <v-col cols="12">
      <v-menu
        ref="menu"
        v-model="menu"
        :close-on-content-click="false"
        :return-value.sync="date"
        transition="scale-transition"
        offset-y
        min-width="290px"
      >
        <template v-slot:activator="{ on, attrs }">
          <v-text-field v-model="date" label="表示する日付" readonly v-bind="attrs" v-on="on"></v-text-field>
        </template>
        <v-date-picker v-model="date" no-title scrollable>
          <v-spacer></v-spacer>
          <v-btn text color="primary" @click="menu = false">Cancel</v-btn>
          <v-btn text color="primary" @click="$refs.menu.save(date)">OK</v-btn>
        </v-date-picker>
      </v-menu>
    </v-col>
  </v-row>
</template>
<script>
export default {
  name: "Date",

  components: {},

  data: () => ({
    // date: new Date().toISOString().substr(0, 10),
    menu: false,
    modal: false,
    menu2: false,
    chenging: false
  }),
  methods: {
    submitDate(date) {
      this.chenging = true;
      this.$store
        .dispatch("getData", date)
        .then(() => {
          this.chenging = false;
        })
        .catch(() => {
          console.log("Error of server");
        });
    }
  },
  computed: {
    date: {
      get() {
        const date = this.$store.state.date;
        // console.log(Date(date));
        if (!date) {
          return new Date().toISOString().substr(0, 10);
        } else {
          return date;
        }
        // return this.value;
      },
      set(date) {
        // console.log(date);
        this.$store.commit("SET_DATE", date);
        this.submitDate(date);
      }
    }
  }
};
</script>
<style lang="stylus" scoped></style>