// import Scheduler from './components/Scheduler.vue'
import Home from './components/Home.vue'
import NotFound from './components/NotFound.vue'

export const routes = [
    // { path: '/scheduler', component: Scheduler },
    { path: '/', component: Home},
    { path: '*', component: NotFound }
]