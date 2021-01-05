import Home from './components/Home.vue'
import NotFound from './components/NotFound.vue'

export const routes = [
    { path: '/', component: Home},
    { path: '*', component: NotFound }
]