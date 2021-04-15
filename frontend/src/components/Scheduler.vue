<template>
  <div>
    <table class="my-table">
      <thead>
        <tr>
          <th></th>
          <th v-for="track in col_header_list" :key="track['id']" class="chart-header"> {{ track.display_name}}</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="time in time_list" :key="time">
          <th scope="row" class="chart-time">{{ time }}</th>
          <td v-for="track in col_header_list" :key="track['id']" class="chart-body">
            <div style="height:50px">
              <template v-if="event_time_map[track.display_name].time_map[time].reserved"> 
                <div :ref="event_time_map[track.id].time_map[time].event_data.name" class="chart-item">
                  {{ event_time_map[track.id].time_map[time].event_data.name }}
                </div>
              </template>
            </div>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios'
import Vue from 'vue'
export default {
  data () {
    return {        
      col_header_list:[], 
      curr_date: "", 
      event_list: [],
      time_list: [],
      event_time_map:{},
      timepicker_start: 7,
      timepicker_end: 18,
    };
  },
  methods: {    
    generateTimes(){
      for(let i = this.timepicker_start; i <= this.timepicker_end; i++){
        this.time_list.push(i+":00")     
      }
    },
    gen_header_list(){
      for(let i = 0; i <8; i++){
        this.col_header_list.push({id:`${i}`, display_name:`Track${i}`})
      }
    },
    gen_event_time_map(){
      console.log(this.col_header_list)
      for(let track of this.col_header_list){
        let one_track_event_list = this.event_list.filter(event => { return event.track === track.display_name })
        let time_map = {}
        for(let event of one_track_event_list){ 
          let time = new Date(event.start_time)
          let hour = time.getHours()
          let min = time.getMinutes()
          if (min == 0) {
            min = `${min}0`
          }
          let time_hh_mm = `${hour}:${min}`
          console.log(min)
          
          Vue.set(time_map,time_hh_mm,{reserved: true, event_data:[event]})
        }
        for(let time of this.time_list){
          if(!time_map[time]) {
             Vue.set(time_map,time,{reserved: false})
          }
        }
        Vue.set(this.event_time_map,track.display_name,{time_map:time_map})
      }
        console.log(this.event_time_map)
        this.setHeight()
    },
    setHeight(){ 
      this.$nextTick(function () {
        console.log(this.$refs)
        for(let res of this.res_list){
          if (this.$refs[res.id]){
            this.$refs[res.id][0].style.height = `${res.time_block_count * 50}px`
            // if(res.data.user_id == this.curr_user_id){
            //   this.$refs[res.id][0].classList.value = 'chart-item-blue'
            // }
          }
        }
      })
    },
    get_events_today(){
      let today = new Date();
      let month = today.getMonth() + 1 //mm
      let day = today.getDate() //dd
      let year = today.getFullYear() //yyyy
      if (day < 10) day = '0' + day
      if (month < 10) month = '0' + month
      this.curr_date = year + '-' + month + '-' + day + " 00:00:00"
      // console.log(this.curr_date)
      let date_obj = { date:this.curr_date }
      axios
        .post('http://127.0.0.1:5000/get_today_events', date_obj)
        .then(response => {
          this.event_list = JSON.parse(response.data)
          console.log(this.event_list)   
          this.gen_event_time_map()
          
        })
        .catch(err =>{
          console.log(err)
        })
    },
  },
  mounted(){
    this.get_events_today()
    this.gen_header_list()
    this.generateTimes();
    // console.log(this.col_header_list)
  }
}
</script>

<style>
  .my-table {
    margin-top: 10px;
    table-layout: fixed;
    border-bottom: 1px solid rgba(0,0,0,0.45);

  } 
  table.my-table th {
    border: 1px solid black;
    padding: 7px;
    text-align: center;
  }
  table.my-table td {
    text-align: center;
  }
  .chart-body{
    background-color: #dcdcdc;
    border-right: 1px solid rgba(0,0,0,0.45);
  }
  .chart-body:nth-of-type(2n){
    background-color: #bbbbbb;
  }
  .chart-header{
    color: #ffffff;
    background-color: #708090 !important;
    width:100px;
    padding: 5px;
    font-size: 13px;
    font-weight: bold;
  }
  .chart-time{
    background-color:#808080;
    color:#fff;
    padding: 20px 0;
    text-align: center;
    align-self: center;
    font-size: 13px;
  }
  .chart-item {
    background-color: #0080FF;
    color: #ffffff;
    text-align: center;
    overflow:hidden;
    position: relative;
    border: 1px solid rgb(110, 110, 110);
    border-radius: 5px;
    margin: 2px;
    padding-top: 15px;
  }
</style>