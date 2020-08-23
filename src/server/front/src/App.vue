<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <h1>terapyon CO2 モニタ</h1>
    </v-app-bar>

    <v-main>
      <Monitor />
    </v-main>
  </v-app>
</template>

<script>
import Monitor from "./components/Monitor";

export default {
  name: "App",

  components: {
    Monitor
  },

  data: () => ({
    //
  })
};
</script>