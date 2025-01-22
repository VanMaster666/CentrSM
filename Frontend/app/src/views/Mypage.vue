<template>
    <Message severity="contrast" variant="simple">USERS</Message>
    <div>
      <DataTable :value="users" :paginator="true" :rows="3" header="Users">
        <Column field="id" header="ID" />
        <Column field="last_name" header="Фамилия" />
        <Column field="name" header="Имя" />
        <Column field="email" header="E-mail" />
        <Column field="phone" header="Phone" />
      </DataTable>
    </div>
    <div style="margin-top:20px">
        <Message severity="contrast" variant="simple">ROLES</Message>
    </div>
    <div>
      <DataTable :value="roles" :paginator="true" :rows="5" header="Roles">
        <Column field="id" header="ID" />
        <Column field="name" header="Название" />
        <Column field="user" header="Пользователь" />
        <Column field="description" header="Описание" />
      </DataTable>
    </div> 
</template>
  
<script>
import axios from 'axios';
import Column from 'primevue/column';
import DataTable from 'primevue/datatable';

    export default {
        components: {
        DataTable,
        Column,
        },
        data() {
        return {
            users: [], // Массив для хранения данных пользователей
            roles: [],
        };
        },
        mounted() {
        this.fetchUsers(); // Загрузка данных при монтировании компонента
         this.fetchRoles();
        },
        methods: {
        async fetchUsers() {
            try {
            const response_users = await axios.get('http://127.0.0.1:5000/users'); // Запрос к API
            this.users = response_users.data; // Предполагаем, что данные находятся в response.data
            } catch (error) {
            console.error('Ошибка при загрузке данных:', error);
            }
        },
        async fetchRoles() {
            try {
            const response_roles = await axios.get('http://127.0.0.1:5000/roles'); // Запрос к API
            this.roles = response_roles.data; // Предполагаем, что данные находятся в response.data
            } catch (error) {
            console.error('Ошибка при загрузке данных:', error);
            }
        },
        },
    };

</script>
  
