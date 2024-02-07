css = '''
<style>
.chat-message {
    padding: 0.5rem;
    border-radius: 1.55rem;
    margin-bottom: 0.8rem;
    display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 6%;
}
.chat-message .avatar img {
  max-width: 50px;
  max-height: 50px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  display: flex;
  align-items: center;
  justify-content: left;
  width: 100%;
  padding: 0 1.5rem;
  color: #fff;
}

.user-icon {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    background-color: gray;

.card {
  box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
  transition: 0.3s;
  width: 40%;
  border-radius: 5px;
  background-color: gray;
}

.card:hover {
  box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
}

img {
  border-radius: 5px 5px 0 0;
}

.container {
  padding: 2px 16px;
}
'''

button_template = '''
<div class="button">
    <div class="avatar">
        <img src="https://cdn-icons-png.flaticon.com/512/9131/9131529.png" style="max-height: 50px; max-width: 50px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

card_template = '''
<div class="card">
  <img src="https://cdn-icons-png.flaticon.com/512/9131/9131529.png" alt="Avatar" style="width:10%">
  <div class="container">
    <h4><b>Jane Doe</b></h4> 
    <p>Interior Designer</p> 
  </div>
</div>
'''