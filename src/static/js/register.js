const { createApp, ref } = Vue;

const app = createApp({
    setup() {
        const username = ref('');
        const email = ref('');
        const password = ref('');
        const confirmPassword = ref('');
        const loading = ref(false);
    
        const register = async () => {
            
          if (password.value !== confirmPassword.value) {
            alert('Passwords do not match!');
            return;
          }
    
          loading.value = true;
    
          try {
            // Simulate API call
            const response = await fetch('/api/user/auth/register/', {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify({
                username: username.value,
                email: email.value,
                password: password.value,
              }),
            });
    
            if (!response.ok) {
              throw new Error('Registration failed');
            }
    
            const data = await response.json();
            console.log(data);
    
            // Clear the form after successful registration
            username.value = '';
            email.value = '';
            password.value = '';
            confirmPassword.value = '';
            alert('Registration successful!');
          } catch (error) {
            console.error(error);
            alert('An error occurred during registration.');
          } finally {
            loading.value = false;
          }
        };
    
        return {
          username,
          email,
          password,
          confirmPassword,
          loading,
          register,
        };
      },
});

app.mount('#app');
