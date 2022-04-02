import os
import interactions


TESTING_SERVERS=[941233178729938955]

bot = interactions.Client(token=os.environ['TOPIC_MAKERTM_TOKEN'])


@bot.command(name="ping", description="ping", scope=TESTING_SERVERS)
async def ping(ctx: interactions.CommandContext):
    await ctx.send("pong!")


@bot.command(
    name="thread", 
    description="Makes a thread of the specified options", 
    scope=TESTING_SERVERS,
    options = [
        interactions.Option(
            name="name",
            description="Name of the thread",
            type=interactions.OptionType.STRING,
            required=True
        ),
        interactions.Option(
            name="role",
            description="Role to mention in the thread",
            type=interactions.OptionType.MENTIONABLE,
            required=True
        ),
        interactions.Option(
            name="channel",
            description="Channel to create the thread, if empty then it will be created in the current channel",
            type=interactions.OptionType.CHANNEL
        )
    ])
async def thread(ctx: interactions.CommandContext, name: str, role, channel=None):
    if channel == None:
        print("user did not chose a channel")
        channel = await ctx.get_channel()
    else:
        print("user chose a channel")
    print(channel)
    await ctx.send(channel.mention)
    thread = await channel.create_thread(name=name)
    await thread.send(f"```{name}```")
    await thread.send(role.mention)
    await ctx.send(f"{thread.mention} has been created!")
    

bot.start()