from telegram import Update
from telegram.ext import ApplicationBuilder
from telegram.ext import CommandHandler
from telegram.ext import ContextTypes
from telegram.ext import Updater
from telegram.ext import filters
from telegram.ext import MessageHandler
import random




async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


tableForMove = [['-', '-', '-', '|  1'],
                ['-', '-', '-', '|  2'],
                ['-', '-', '-', '|  3'],
                ['a', 'b', 'c', ' ']]

async def PrintTableForMove(update: tableForMove, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
            f'Таблица для ходов:\n------------------------------------\n\
            {tableForMove[0][0]}        {tableForMove[0][1]}        {tableForMove[0][2]}         {tableForMove[0][3]}\n\
            {tableForMove[1][0]}        {tableForMove[1][1]}        {tableForMove[1][2]}         {tableForMove[1][3]}\n\
            {tableForMove[2][0]}        {tableForMove[2][1]}        {tableForMove[2][2]}         {tableForMove[2][3]}\n\
            {tableForMove[3][0]}        {tableForMove[3][1]}        {tableForMove[3][2]}         {tableForMove[3][3]}')


def Game(table, context: ContextTypes.DEFAULT_TYPE):
    PrintTableForMove(tableForMove)
    # случайным образом выбирается чей первый ход
    if random.randint(0, 1) == 1:
        firstMove = 1
        # table.message.reply_text('asd')
        print('Первых ход за игроком.')
    else:
        firstMove = 0
        print('Первых ход за компьютером.')
    # случайным образом выбирается кто чем играет (ноликами или крестиками)
    if random.randint(0, 1) == 1:
        userValue = 'X'
        print('Ты ставишь крестики (X).')
        botValue = 'O'
    else:
        userValue = 'O'
        print('Ты ставишь нолики (O).')
        botValue = 'X'

    # задаем начальное количество сделанных ходов, победителя и список доступных ходов
    moves = 0
    winner = None
    listOfMoves = ['a1', 'b1', 'c1', 'a2', 'b2', 'c2', 'a3', 'b3', 'c3']

    while len(listOfMoves) > 0:

        if firstMove == 1:  # ходит человек
            move = CheckInput(input('Куда ставим?: '), listOfMoves, table)
            if move == 'a1':
                table[0][0] = userValue
            elif move == 'b1':
                table[0][1] = userValue
            elif move == 'c1':
                table[0][2] = userValue
            elif move == 'a2':
                table[1][0] = userValue
            elif move == 'b2':
                table[1][1] = userValue
            elif move == 'c2':
                table[1][2] = userValue
            elif move == 'a3':
                table[2][0] = userValue
            elif move == 'b3':
                table[2][1] = userValue
            elif move == 'c3':
                table[2][2] = userValue
            listOfMoves.remove(move)  # удаляем из списка ходов сделанный ход
            moves += 1
            firstMove = 0
            PrintTableForMove(table)
            print(f'Ты ставишь крестики ({userValue}).')

            # обработка победителя
            winner = WhoWins(table)
            if winner == userValue:
                print(f'Поздравляю, вы выиграли, играя за -> {winner}')
                return [1, 0]

        elif firstMove == 0:  # ходит бот
            move = random.choice(listOfMoves)
            if move == 'a1':
                table[0][0] = botValue
            elif move == 'b1':
                table[0][1] = botValue
            elif move == 'c1':
                table[0][2] = botValue
            elif move == 'a2':
                table[1][0] = botValue
            elif move == 'b2':
                table[1][1] = botValue
            elif move == 'c2':
                table[1][2] = botValue
            elif move == 'a3':
                table[2][0] = botValue
            elif move == 'b3':
                table[2][1] = botValue
            elif move == 'c3':
                table[2][2] = botValue
            listOfMoves.remove(move)  # удаляем из списка ходов сделанный ход
            moves += 1
            firstMove = 1
            PrintTableForMove(table)
            print(f'Ты ставишь крестики ({userValue}).')

            # обработка победителя
            winner = WhoWins(table)
            if winner == botValue:
                print(
                    f'К сожалению, эту партию выиграл БОТ, играя за -> {winner}')
                return [0, 1]
    print(f'В этот раз ничья.')
    return [0, 0]  # возвращает ничью

# Метод определяющий победителя (X или O) и возвращающий это значение
def WhoWins(table):
    for x in range(0, 3):
        if table[x][0] == table[x][1] == table[x][2] != ' ':
            print('Игра окончена.')
            return table[x][0]
    for y in range(0, 3):
        if table[0][y] == table[1][y] == table[2][y] != ' ':
            print('Игра окончена.')
            return table[0][y]
    if table[0][0] == table[1][1] == table[2][2] != ' ':
        print('Игра окончена.')
        return table[1][1]
    elif table[0][2] == table[1][1] == table[2][0] != ' ':
        print('Игра окончена.')
        return table[1][1]


# Метод который обрабатывает неправильный пользовательский ввод (или не то поле, или в это поле уже поставили)
def CheckInput(userInput, listOfMoves, table):
    if userInput in listOfMoves:
        return userInput
    else:
        print(PrintTableForMove(table))
        print('Не верный ввод. Повторите!')
        newUserInput = input('Куда ставим?: ')
        return CheckInput(newUserInput, listOfMoves, table)


# result = Game(tableForMove)
# print(f'Результат игры (игрок,бот) = {result}')


app = ApplicationBuilder().token("5489651106:AAFJJZ6fP2GqzgVPv64NrtDy9NGH9wxQKmk").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("start_game", PrintTableForMove))


print('server start')
app.run_polling()
