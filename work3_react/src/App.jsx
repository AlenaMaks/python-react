// 2) Вывести список пользователей, по нажатию на пользователя справа или снизу будет 
// выведен блок с написанными им постами, структура карточки, title, body

import { useState, useEffect } from 'react'; // подключаем хуки
import './App.css';

function App() {
  const [users, setUsers] = useState([]); // состояние для пользователей
  const [posts, setPosts] = useState([]); // для постов
  const [selectedUser, setSelectedUser] = useState(null); // для конкретного пользователя

  useEffect(() => {
    fetch('https://jsonplaceholder.typicode.com/users') // данные о пользователях
      .then(response => response.json())
      .then(data => {setUsers(data);}); 
      // перобразуем json и функция изменения состояния setUsers заменяет элементы в users
  }, []);

  // console.log(users);

  useEffect(() => {
    fetch('https://jsonplaceholder.typicode.com/posts') // данные о постах
      .then(response => response.json())
      .then(data => {setPosts(data);}); // аналогично с users
  }, []);

  // console.log(posts);

  return (
    <div>
      <h1>Пользователи и посты. Work 3</h1>
      <div className="container">
        <div className="users-block">
          <h2>Пользователи</h2>
          {users.map(user => {
            const userPosts = posts.filter(
              post => post.userId === user.id // сверяем для вывода кол-ва постов у юзера
            );
            return ( // в ходе filter возвращаем карточку где и указываем количество
              <div key={user.id} className="user-card">
                <h3
                  onClick={() => setSelectedUser(user)} // меняем состояние selectedUser при нажатии
                  style={{ cursor: 'pointer' }}
                > {user.name} </h3>
                <p>Постов: {userPosts.length}</p>
              </div>
            );
          })}
        </div>
        <div className="posts-block">
          {selectedUser ? ( // если конкретный пользователь выбран (if else конструкция)
            <div>
              <h2> Посты пользователя {selectedUser.name} </h2>
              {posts
                .filter(post => post.userId === selectedUser.id) // ищем посты выбранного юзера
                .map(post => ( // проходит по всем элементам
                  <div key={post.id} className="post-card">
                    <h3>{post.title}</h3>
                    <p>{post.body}</p>
                  </div>
                ))}
            </div>
          )
          : (<h2>Выберите пользователя</h2>)
          }
        </div>
      </div>
    </div>
  );
}

export default App;
