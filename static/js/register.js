const { createApp, ref } = Vue;

console.log('HELLO: ', CSRF_TOKEN);

const app = createApp({
  setup() {
    const phone = ref('');
    const email = ref('');
    const password = ref('');
    const confirmPassword = ref('');
    // const loading = ref(false);
    const firstName = ref('');
    const lastName = ref('');

    const register = async () => {
      console.log('Registering...');
      if (password.value !== confirmPassword.value) {
        alert('Passwords do not match!');
        return;
      }

      // loading.value = true;

      try {
        // Data to be sent in the request
        const requestData = {
          phone: phone.value,
          email: email.value,
          password: password.value,
          confirm_password: confirmPassword.value,
          first_name: firstName.value,
          last_name: lastName.value,
        };

        console.log('Request Data:', requestData);

        // API call using Axios
        const response = await axios.post('/api/user/auth/register/', requestData, {
          headers: { 
            'Content-Type': 'application/json',
            'X-CSRFToken': CSRF_TOKEN,
          },
        });

        console.log('Response:', response.data);

        // Clear the form after successful registration
        phone.value = '';
        email.value = '';
        password.value = '';
        confirmPassword.value = '';
        firstName.value = '';
        lastName.value = '';

        alert('Registration successful!');
      } catch (error) {
        console.error('Error:', error.response?.data || error.message);
        alert('An error occurred during registration.');
      } 
      // finally {
      //   loading.value = false;
      // }
    };

    return {
      phone,
      email,
      password,
      confirmPassword,
      firstName,
      lastName,
      // loading,
      register,
    };
  },
});

app.mount('#app');
