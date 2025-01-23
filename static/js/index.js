const { createApp, ref } = Vue
console.log('HELLO: ', IS_LOGGED_IN);

  createApp({
    setup() {
      const isLoggedIn = ref(IS_LOGGED_IN);
      console.log('Logedin: ', isLoggedIn.value);
      
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
      ]);
      const products = ref([
        {
          product_name: 'Abc',
          description: 'this is Discription',
          quantity: 3,
          img:'',
        }
      ])
      return {
        categories,
        isLoggedIn,
      }
    }
  }).mount('#app')