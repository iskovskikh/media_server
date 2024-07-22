<template>
  <div>

    <table>
      <tr>
        <th>oid</th>
        <th>login</th>
        <th>full_name</th>
        <th>company</th>
        <th>position</th>
        <th></th>
      </tr>
      <tr v-for="item in users.items" :key="item.oid" @click="alert(index)">
        <td>{{ item.oid }}</td>
        <td>{{ item.login }}</td>
        <td>{{ item.full_name }}</td>
        <td>{{ item.company }}</td>
        <td>{{ item.position }}</td>
        <td>
          <NuxtLink :to="`/user/${item.oid}`">редактировать</NuxtLink>
        </td>
      </tr>
    </table>
  </div>
</template>

<script setup>

const config = useRuntimeConfig();

const {data: users} = await useFetch(`${config.public.API_BASE_URL}/api/user/`)

</script>

<style>

table {
  border-collapse: collapse;
}

tr {
  border-bottom: 1pt solid black;
}

td {
  padding: 8px;
}

</style>