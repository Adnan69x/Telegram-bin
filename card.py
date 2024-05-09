from telethon.sync import TelegramClient
import random
import asyncio

# Replace 'YOUR_API_ID', 'YOUR_API_HASH', 'YOUR_BOT_TOKEN', and 'YOUR_CHANNEL' with your actual values
API_ID = '27913018'
API_HASH = '04e2f4e414cdabe52ad985adaa6cfe09'
BOT_TOKEN = '6826415817:AAG1alKRjdc20hXtYtVT20yowAR2nCnHLWQ'
CHANNEL = '-1002110033979'

def generate_card_number():
    # Generate a random 16-digit card number
    card_number = ''.join(str(random.randint(0, 9)) for _ in range(16))
    return card_number

def validate_card_number(card_number):
    # Perform a simple Luhn algorithm check for card number validity
    digits = [int(digit) for digit in card_number]
    checksum = sum(digits[::-2] + [sum(divmod(2 * d, 10)) for d in digits[-2::-2]])
    return checksum % 10 == 0

def generate_and_send_card(client, num_cards):
    group_cards = []
    for _ in range(num_cards):
        card_number = generate_card_number()
        while not validate_card_number(card_number):
            card_number = generate_card_number()
        group_cards.append(card_number)
    message = "Generated and validated card numbers:\n"
    for card_number in group_cards:
        message += card_number[:8] + "xxxxxxxx | xx | xx | xxx\n"
    client.send_message(CHANNEL, message)

async def main():
    client = TelegramClient('session_name', API_ID, API_HASH)
    await client.start(bot_token=BOT_TOKEN)
    num_cards = int(input("Enter the number of cards to generate and send: "))
    await generate_and_send_card(client, num_cards)
    await client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
