import time
import pytz
import datetime as dt
import discord
import asyncio

from datetime import timedelta
from pytz import timezone
from pytz import common_timezones
from discord.ext import commands

cancelled = 0
Tz = {
    'PST': timezone('America/Los_Angeles'),
    'CEST': timezone('Europe/Berlin'),
    'EST': timezone('America/New_York'),
    'UTC': pytz.utc
}
# UTC = pytz.utc
# CEST = timezone('Europe/Berlin')
# PST = timezone('America/Los_Angeles')
# EST = timezone('America/New_York')
# print(CEST.zone, UTC.zone, PST.zone, EST.zone)


class Countdown(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def settime(self, ctx, eventname, time1, time2, timezone1):
        h, m = time2.split(':')
        m = int(m)
        h = int(h)

        month, day, year = time1.split('/')
        month = int(month)
        day = int(day)
        year = int(year)

        # datetimeFormat = '%Y-%m-%d %H:%M:%S'
        # timezoneend = pytz.timezone(Tz[timezone1])

        date = dt.datetime(year, month, day, h, m,)
        cur_date = dt.datetime.now(Tz[timezone1])
        cur_date.replace(microsecond=0)

        print(cur_date)
        print(date)

        aware_date = date.astimezone(Tz[timezone1])
        aware_date.replace(microsecond=0)

        diff = aware_date-cur_date.replace(microsecond=0)
        print(diff)
        days, hours, minutes,seconds = diff.days, diff.seconds // 3600, diff.seconds % 3600 / 60.0, diff.seconds % 60
        print(seconds)
        time = await ctx.send(f'{eventname} Countdown \nDays left: {int(days)} \nHours left: {int(hours)} \nMinutes left: {int(minutes)} \n Seconds left: {seconds}')
        global cancelled
        cancelled = 0
        while diff.seconds != 0 & cancelled == 0:
            if cancelled == 1:
                break
            if seconds <= 0 and minutes <= 0 and hours <= 0 and days <= 0:
                break
            if days < 0:
                days = 0
                minutes = 0
                hours = 0
                seconds = 0
                await time.edit(
                    content=f'{eventname} Countdown \nDays left: {int(days)} \nHours left: {int(hours)} \nMinutes left: {int(minutes)} \n Seconds left: {seconds}')
                print("Stopping")
                break

            await asyncio.sleep(60)

            cur_date = dt.datetime.now(Tz[timezone1])
            aware_date = date.astimezone(Tz[timezone1])
            diff = aware_date - cur_date.replace(microsecond=0)

            days, hours, minutes, seconds = diff.days, diff.seconds // 3600, diff.seconds % 3600 / 60.0, diff.seconds % 60
            await time.edit(content = f'{eventname} Countdown \nDays left: {int(days)} \nHours left: {int(hours)} \nMinutes left: {int(minutes)} \n Seconds left: {seconds}')

    @commands.command()
    async def stop(self, ctx):
        global cancelled
        cancelled = 1
        await ctx.send("Stopping timer")


def setup(client):
    client.add_cog(Countdown(client))