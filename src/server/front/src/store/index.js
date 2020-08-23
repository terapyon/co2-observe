import Vue from "vue";
import Vuex from "vuex";
import FetchData from "@/services/FetchData.js"
import { TimeData } from "../modules"

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    date: null,
    timeData: []
  },
  mutations: {
    SET_DATE: function (state, date) {
      state.date = date
    },
    SET_TIMEDATA: function (state, timeData) {
      state.timeData = timeData.map(d => new TimeData(d.time, d.co2, d.temperature))
      // .sort(function (a, b) {
      //   return parseInt(a.time) - parseInt(b.time)
      // })
    },
  },
  actions: {
    getData({ commit }, date) {
      return FetchData.postFetch(date).then((timeData) => {
        commit("SET_TIMEDATA", timeData.data)
      }).catch(() => {
        console.log("Error of server for getData");
      });;
    },
  },
  modules: {}
});
