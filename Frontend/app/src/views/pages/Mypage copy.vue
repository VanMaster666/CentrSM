<template>
    <Message severity="contrast" variant="simple">USERS</Message>
    <div>
      <DataTable :value="users" :paginator="true" :rows="12" header="Users">
        <Column field="id" header="ID" />
        <Column field="last_name" header="Фамилия" />
        <Column field="name" header="Имя" />
        <Column field="email" header="E-mail" />
        <Column field="phone" header="Phone" />
      </DataTable>
    </div>
</template>
  
<script>
import axios from 'axios';
import Column from 'primevue/column';
import DataTable from 'primevue/datatable';
import Message from 'primevue/message';

    export default {
        components: {
        DataTable,
        Column,
        },
        data() {
        return {
            users: [], // Массив для хранения данных пользователей
        };
        },
        mounted() {
        this.fetchUsers(); // Загрузка данных при монтировании компонента
        },
        methods: {
        async fetchUsers() {
            try {
            const response = await axios.get('http://127.0.0.1:5000/api/users'); // Запрос к API
            this.users = response.data; // Предполагаем, что данные находятся в response.data
            } catch (error) {
            console.error('Ошибка при загрузке данных:', error);
            }
        },
        },
    };
</script>
  
