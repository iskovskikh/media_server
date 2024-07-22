<template>
  <div class="mt">
    <form @submit.prevent="update_user">
      <div class="mb">
        <label>login<input type="text" v-model="login"/></label>
      </div>
      <div class="mb">
        <label>password<input type="text" v-model="password"/></label>
      </div>

      <div class="mb">
        <label>full_name<input type="text" v-model="full_name"/></label>
      </div>

      <div class="mb">
        <label>company<input type="text" v-model="company"/></label>
      </div>

      <div class="mb">
        <label>position<input type="text" v-model="position"/></label>
      </div>

      <button type="submit">Сохранить</button>

    </form>

    <pre> {{ errors }}</pre>

  </div>
</template>

<script setup lang="ts">
const config = useRuntimeConfig();

const router = useRouter();

const route = useRoute();

const {data: user} = await useFetch(`${config.public.API_BASE_URL}/api/user/${route.params.oid}`)

const login       = ref(user.value.login);
const password    = ref('');
const full_name   = ref(user.value.full_name);
const company     = ref(user.value.company);
const position    = ref(user.value.position);

const errors = ref({});

const update_user = async () => {

  //store data with API
  await $fetch(`${config.public.API_BASE_URL}/api/user/${route.params.oid}`, {

    method: 'POST',

    body: {
      login: login.value,
      password: password.value,
      full_name: full_name.value,
      company: company.value,
      position: position.value,
    }
  })
  .then(() => {
    //redirect
    router.push({path: "/"});
  })
  .catch((error) => {

    //assign response error data to state "errors"
    errors.value = error.data
  });
}
</script>

<style>
.mt {
  margin-top: 10px;
}

.mb {
  margin-bottom: 10px;
}
</style>