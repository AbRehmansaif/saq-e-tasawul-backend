const { createApp, ref } = Vue

  createApp({
    setup() {
      const categories = ref([
        {
            img:'/static/img/category-1.jpg',
            name:'Watch',
            description: 'This is watch category',
        },
        {
            img:'/static/img/category-1.jpg',
            name:'T-shirt',
            description: 'This is watch category',
        },
        {
            img:'/static/img/category-1.jpg',
            name:'Cup',
            description: 'This is watch category',
        },
      ])
      return {
        categories
      }
    }
  }).mount('#app')