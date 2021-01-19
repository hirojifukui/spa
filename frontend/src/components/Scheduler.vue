<template>
  <div class="container">
    <div class="chart">
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  props: ['col_header_list'],
  data () {
    return {     
      curr_date: "", 
      event_list: [],
      time_list: [],
      timepicker_start: 7,
      timepicker_end: 18,
    };
  },
  methods: {    
    gen_curr_date(){
      let today = new Date();
      let month = today.getMonth() + 1 //mm
      let day = today.getDate() //dd
      let year = today.getFullYear() //yyyy
      if (day < 10) day = '0' + day
      if (month < 10) month = '0' + month
      this.curr_date = year + '-' + month + '-' + day
    },
    generateTimes(){
      for(let i = this.timepicker_start; i <= this.timepicker_end; i++){
        this.time_list.push(i+":00")     
      }
      let today = new Date();
      let month = today.getMonth() + 1 //mm
      let day = today.getDate() //dd
      let year = today.getFullYear() //yyyy
      if (day < 10) day = '0' + day
      if (month < 10) month = '0' + month
      this.curr_date = year + '-' + month + '-' + day + " 00:00:00"
    },
    createContainer(){
      const chart_div = document.querySelector('.chart')
      chart_div.innerHTML = ''
      let total_col_num = this.col_header_list.length
      let total_row_num = this.time_list.length
      chart_div.style.cssText = 
          "grid-template-columns: [times] 3em repeat(" + total_col_num + ", 1fr); \
           grid-template-rows: [times] auto repeat(" + total_row_num + ", 1fr);"
      let i = 2
      for (let header of this.col_header_list){
        const chart_header_span =  document.createElement('span')
        chart_header_span.id = i-1
        chart_header_span.style.setProperty('grid-column', i)
        chart_header_span.style.setProperty('grid-row', 'times')
        chart_header_span.classList.add('chart-header')
        chart_header_span.classList.add('chart-column')
        chart_header_span.innerHTML = header

        const chart_col_body_span =  document.createElement('span')
        chart_col_body_span.style.cssText = 
            "grid-row: 2/14; grid-column: " + i
        chart_col_body_span.classList.add('chart-col')

        chart_div.appendChild(chart_header_span)
        chart_div.appendChild(chart_col_body_span)
        i++
      }
      i = 2
      for (let time of this.time_list){
        const chart_time_span = document.createElement('span')
        chart_time_span.style.cssText = 
            "grid-column: times; grid-row: " + i;
        chart_time_span.classList.add('chart-time')
        chart_time_span.innerHTML = time  
        chart_div.appendChild(chart_time_span)
        i++
      }
    },
    addItemByObject(event){
      let start_time_date = new Date(event.start_time * 1000).getHours()
      let end_time_date = new Date(event.end_time * 1000).getHours()
      const chart_div = document.querySelector('.chart')
      const item_div = document.createElement('span')
      let track = this.col_header_list.indexOf(event.track) + 2
      let start_row = this.time_list.indexOf(start_time_date + ":00") + 2
      let end_row = this.time_list.indexOf(end_time_date + ":00") + 2
      item_div.style.cssText = 
            "grid-column: " + track + "; grid-row: " + start_row + "/" + end_row;
      item_div.innerHTML = event.name
      item_div.classList.add('chart-item')
      chart_div.appendChild(item_div)
    },
    async get_events_today(){
      axios
        .get('http://127.0.0.1:5000/get_today_events', {params:{ date:this.curr_date }})
        .then(response => {
          this.event_list = JSON.parse(response.data)
          for(let event of this.event_list){
            this.addItemByObject(event);
          }
        })
        .catch(err =>{
          console.log(err)
        })
    },
  },
  mounted(){
    this.generateTimes();
    this.get_events_today();
    this.createContainer();

  }
}
</script>

<style>
  .container {
    max-width: 1400px;
    min-width: 650px;
  } 
  .chart{
    display: grid;
    border: 1px solid #000;
    position: relative;
    overflow: hidden;
  }
  .chart-col{
    background-color: #dcdcdc;
    border-left: 1px solid rgba(0,0,0,0.3);
  }

  .chart-header{
    color: #ffffff;
    background-color: #708090 !important;
    border-left: 1px solid rgba(0,0,0,0.3);
    border-bottom: 1px solid rgba(0,0,0,0.3);
    text-align:center;
    align-self: center;
    padding: 5px;
    font-size: 13px;
    font-weight: bold;
  }
  .chart-time{
    background-color:#808080;
    color:#fff;
    border-top: 1px solid rgba(0,0,0,0.3);
    padding: 20px 0;
    text-align: center;
    align-self: center;
    font-size: 13px;
  }
  .chart-item {
    color: #ffffff;
    text-align: center;
    background-color: #0080FF;
    overflow: hidden;
    position: relative;
    border-radius: 5px;
    margin: 2px;
    margin-left: 3px;
    padding-top: 15px;
  }
</style>