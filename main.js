require('dotenv').config();

const Discord = require('discord.js');
const client = new Discord.Client();

client.on('ready', () => {
  console.log(`Bot is online! Logged in as ${client.user.tag}`);
});

client.on('message', message => {
  if (message.content === '!hello') {
    message.reply('Hello!');
  }
});

client.login(process.env.TOKEN);