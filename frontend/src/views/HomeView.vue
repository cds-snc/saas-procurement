<script setup lang="ts">
import { ref, onMounted } from 'vue'
const googleLogs = ref({ logs: [] })
onMounted(() => {
  fetch('http://127.0.0.1:8000/en/manage_saas/google_logs/', {
    method: 'GET',
    headers: { 'Content-Type': 'application/json' }
  })
    .then((res) => res.json())
    .then((data) => {
      console.log(JSON.parse(data))
      googleLogs.value.logs = JSON.parse(data)
    })
    .catch((err) => console.log(err))
})
</script>

<template>
  <main id="content">
    <h1>All login Events with Google credentials</h1>
    <p>
      This is the list of all logins to external apps or products using an individuals CDS google
      credentials
    </p>
    <p>
      There are currently {{ googleLogs.logs.length }} logins records in the database. This is a
      list of the last
    </p>
    <table class="table table-responsive-lg table-hover table-bordered">
      <thead>
        <tr>
          <th>Email</th>
          <th>Date</th>
          <th>App Name</th>
          <th>App Type</th>
          <th>Event Name</th>
        </tr>
        <tr v-for="log in googleLogs.logs" :key="log.id">
          <td>{{ log.fields.user_email }}</td>
          <td>{{ log.fields.time_generated }}</td>
          <td>{{ log.fields.application_name }}</td>
          <td>{{ log.fields.client_type }}</td>
          <td>{{ log.fields.event_name }}</td>
        </tr>
      </thead>

      <tbody></tbody>
    </table>
  </main>
</template>
