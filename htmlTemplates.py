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
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://investment-s3.unitedtraders.io/shares/BAC.svg" style="max-height: 50px; max-width: 50px; border-radius: 1.2rem; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <div class="user-icon">
        </div> 
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''