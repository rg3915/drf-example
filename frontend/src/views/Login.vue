<template>
  <div class="container">
    <div class="columns">
      <div class="column is-4 is-offset-4">
        <h1 class="title">Login</h1>

        <form @submit.prevent="submitForm">
          
          <div class="field">
            <label>Usuário</label>
            <div class="control">
              <input type="text" name="username" class="input" v-model="username" autofocus>
            </div>
          </div>

          <div class="field">
            <label>Senha</label>
            <div class="control">
              <input type="password" name="password" class="input" v-model="password">
            </div>
          </div>

          <div class="notification is-danger" v-if="errors.length">
            <p v-for="error in errors" :key="error">{{ error }}</p>
          </div>

          <div class="field">
            <div class="control">
              <button class="button is-success">Entrar</button>
            </div>
          </div>

        </form>

      </div>
    </div>
  </div>
</template>

<script>
  import axios from 'axios'

  export default {
    name: 'Login',
    data() {
      return {
        username: '',
        password: '',
        errors: []
      }
    },
    methods: {
      async submitForm() {
        axios.defaults.headers.common['Authorization'] = ''
        localStorage.removeItem('token')
        const formData = {
          username: this.username,
          password: this.password
        }
        await axios
          .post('/api/v1/auth/token/login/', formData)
          .then(response => {
            const token = response.data.auth_token
            axios.defaults.headers.common['Authorization'] = 'Token ' + token
            localStorage.setItem('token', token)
          })
          .catch(error => {
            if (error.response) {
              for (const property in error.response.data) {
                this.errors.push(`${property}: ${error.response.data[property]}`)
              }
            } else if (error.message) {
              this.errors.push('Algo deu errado. Por favor tente novamente!')
            }
          })
      }
    }
  }
</script>