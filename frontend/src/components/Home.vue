<template>
  <div>
    <div class="flex-column d-flex container">
      <div class="row">
        <div class="col">
          Showing events for {{ curr_date }}
        </div>
        <div class="col">
          <button type="button" class="btn add" data-toggle="modal" data-target="#addEvent">
            Add Event
          </button>
          <div class="modal fade" id="addEvent" tabindex="-1" role="dialog">
            <app-add-event :col_header_list="col_header_list"></app-add-event>
          </div>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col">
        <app-scheduler class="chart" 
            :col_header_list="col_header_list"> 
        </app-scheduler>
      </div>
    </div>
  </div>
</template>

<script>
import AddEvent from './AddEvent.vue'
import Scheduler from './Scheduler.vue'


export default {
  data(){
    return{
      col_header_list:[],
      curr_date: ""
    }
  },
  components: {
    appAddEvent: AddEvent,
    appScheduler: Scheduler
  },
  methods: {    
    gen_header_list(){
      for(let i = 0; i <8; i++){
        this.col_header_list.push({id:`${i}`, display_name:`Track${i}`})
      }
    },
    gen_curr_date(){
      let today = new Date();
      let month = today.getMonth() + 1 //mm
      let day = today.getDate() //dd
      let year = today.getFullYear() //yyyy
      if (day < 10) day = '0' + day
      if (month < 10) month = '0' + month
      this.curr_date = year + '-' + month + '-' + day
    }
  },
  mounted(){
    this.gen_header_list()
    this.gen_curr_date();
  }
}
</script>

<style scoped>
.chart{
  display: flex;
  justify-content: center;
}
.add{
  width: 148px;
  border-radius: 25px;
  background-color: rgb(34,123,206);
  color:white;
  float: right;
}
</style>