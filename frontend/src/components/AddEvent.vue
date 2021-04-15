<template>
  <div>
    <div class="modal-dialog" role="=document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">New Event</h5>
        </div>
        <div class="modal-body">
          <form>
            <div class="form-group">
              <label class="col-form-label">Event Name: </label>
              <input type="text" class="form-control" v-model.trim="event_name">
            </div>
            <div class="form-group">
              <label class="typo__label">Track: </label>
              <select v-model="track">
                <option v-for="option in col_header_list" :key="option.id">
                  {{ option.display_name }}
                </option>
              </select>
            </div>
            <div class="form-group">
              <div class="row">
                <div class="col-md-6">
                  <label for ="start-time" class="col-form-label">Start Time:  </label>
                  <VueTimePicker
                      format="HH"
                      :hour-range="[[7,17]]"
                      v-model="start_time"
                      hide-disabled-hours>
                  </VueTimePicker>
                </div>
                <div class="col-md-6 ml">
                  <label for ="start-time" class="col-form-label">End Time:  </label>
                  <VueTimePicker
                      format="HH"
                      :hour-range="[[7,17]]"
                      v-model="end_time"
                      hide-disabled-hours>
                  </VueTimePicker>
                </div>
              </div>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-dismiss="modal">Cancel</button>
              <button type="submit" class="btn btn-primary" @click.prevent="submit_modal">Reserve</button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import VueTimePicker from 'vue2-timepicker'
import 'vue2-timepicker/dist/VueTimepicker.css'

export default {
  props: ['col_header_list'],
  components:{
    VueTimePicker
  },
  data (){
    return {
      event_name: "",
      track: "",
      start_time: "",
      end_time: "",

    }
  },
  methods: {
    timestamp_to_epoch(input_time){
      var today = new Date()
      today.setHours(input_time);
      today.setMinutes(0)
      today.setSeconds(0)
      return today.getTime()
    },
    submit_modal(){
      let event_name_is_empty = (this.event_name == "")
      let track_is_empty = (this.track == "")
      let start_time_is_empty = (this.start_time == "")
      let end_time_is_empty = (this.end_time == "")
      if (event_name_is_empty || track_is_empty || start_time_is_empty || end_time_is_empty){
        return alert('Error: you must fill out all required fields!')
      }

      let form_data = {
        name: this.event_name,
        track: this.track,
        start_time: this.timestamp_to_epoch(this.start_time) / 1000,
        end_time: this.timestamp_to_epoch(this.end_time) / 1000
      }
      console.log(form_data)
      this.post_request(form_data)

    },
    post_request(form_obj){
      axios
        .post('http://127.0.0.1:5000/add_event', form_obj)
        .then(res => {
          if(res.data['success'] == 'true'){
            console.log('success')
            history.go(0)
          }
          else if(res.data['success'] == 'false'){
            alert("ERROR: " + res.data['message'])
          }
        })
        .catch(err => {
          console.log(err)
        });
    }
  }
}
</script>
<style scoped>

</style>