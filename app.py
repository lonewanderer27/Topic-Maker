import os
from datetime import date
from keep_alive import keep_alive
import interactions


# TESTING_SERVERS=[941233178729938955, 997532964659404910]

bot = interactions.Client(token=os.environ['ENHANCEDTOPIC_MAKERTM_TOKEN'])
today = date.today()


@bot.command(name="ping", description="ping")
async def ping(ctx: interactions.CommandContext):
    print('%s has sent a ping, so we pong!' %ctx.user.username)
    await ctx.send("pong!")


@bot.command(
    name="thread", 
    description="Makes a thread of the specified options",
    options = [
        interactions.Option(
            name="name",
            description="Name of the thread",
            type=interactions.OptionType.STRING,
            required=True
        ),
        interactions.Option(
            name="role",
            description="Roles to mention in the thread",
            type=interactions.OptionType.MENTIONABLE,
            required=True,
        ),
        interactions.Option(
            name="channel",
            description="Channel to create the thread, if empty then it will be created in the current channel",
            type=interactions.OptionType.CHANNEL
        )
    ])
async def thread(ctx: interactions.CommandContext, name: str, role, channel=None):
    if channel == None:
        channel = await ctx.get_channel()
        channel_name = 'this'
    else:
        channel_name = channel.mention

    thread_created_embed = interactions.Embed(
        title=name,
        description="A topic made by %s for %s channel." %(ctx.user.mention, channel_name),
        thumbnail = interactions.EmbedImageStruct(url=ctx.member.user.avatar_url),
        color = 0x022af5,
        footer = interactions.EmbedFooter(text=today.strftime("%B %d, %Y"))
    )

    if ctx.channel == channel:
        await ctx.send(embeds=thread_created_embed)
    else:
        await ctx.send("%s kindly check your newly created thread in %s channel." %(ctx.user.mention, channel.mention), ephemeral=True)
        await channel.send(embeds=thread_created_embed)

    thread = await channel.create_thread(name=name)
    await thread.send(embeds=thread_created_embed)

    print('%s%s: created thread on channel: %s' %(ctx.user.username, "#"+ctx.member.user.discriminator, channel.name))
    
if __name__ == '__main__':
    keep_alive()
    bot.start()