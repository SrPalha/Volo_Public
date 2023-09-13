# English README - Usage of Buttons and Modal Forms

This bot is a demonstrates the usage of buttons and modal forms in a Discord bot. Here's an overview of the code and its purpose:

## Description
This code represents a Discord bot designed to facilitate the creation of private rooms for user groups. It utilizes buttons and modal forms, built using the Discord.py library, to interact with users and gather information needed for the room creation.

## Features

1. **User Group Rooms**: The bot allows users to request private rooms for their groups. They can fill out a questionnaire to provide the necessary details.

2. **Modal Form**: The bot presents a modal form to users, which includes various questions related to the group room request.

3. **Buttons for Approval and Rejection**: After a user submits the form, a "Aprovar" (Approve) and a "Não Aprovar" (Reject) button are available for moderators or support members to take action on the request.

## Usage

1. When the bot is online, users can initiate the room request process by clicking the "Abrir Questionário" (Open Questionnaire) button.

2. Users complete the modal form by answering the questions provided.

3. Moderators or support members receive an embed message with the user's responses and have the option to either approve or reject the room request using the respective buttons.

4. If approved, the bot notifies the user, and a private room is created for their group.

## Important Note
This bot uses the Discord.py library and requires proper configuration, permissions, and the bot token to run successfully on your Discord server. Ensure you have the necessary permissions and replace `'YOUR_DISCORD_TOKEN'` with your bot's token in the last line of the code.

## Contributions and Customization
Feel free to customize the code to suit your specific requirements or expand its functionality. You can add more questions to the modal form or modify the bot's behavior as needed.

---
