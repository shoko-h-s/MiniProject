import random

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
cards = [i+1 for i in range(10)]
for _ in range(3):
  cards.append(10)

# 初期設定
p1 = random.randint(0, 12)
d1 = random.randint(0, 12)
p2 = random.randint(0, 12)
d2 = random.randint(0, 12)

your_card_1 = cards[p1]
dealer_card_1 = cards[d1]
your_card_2 = cards[p2]
dealer_card_2 = cards[d2]

your_sum = your_card_1 + your_card_2
dealer_sum = dealer_card_1 + dealer_card_2

game_set_flag = False
turn_flag = True

print(f"あなたの手札： {your_card_1}, {your_card_2}　　　合計： {your_sum}")
print(f"ディーラーの手札： {dealer_card_1}, {dealer_card_2}　　　合計： {dealer_sum}\n")

# あなたのターン
while turn_flag:
  user_input = input("カードを引きますか？（y/n）： ")
  # user_input = input("カードを引きますか？ 引く場合は [y] をタイプしてください。： ")
  print()

  if user_input == "y":
    p = random.randint(0, 12)
    your_card = cards[p]
    your_sum += your_card
    print(f"あなたが新しく引いたカードは、{your_card}　　　合計： {your_sum}")

    if your_sum > 21:
      print("Burst！ あなたの負けです。")
      game_set_flag = True
      turn_flag = False

  else:
    turn_flag = False

# コンピュータのターン
if not game_set_flag:
  while dealer_sum < 17:
    d = random.randint(0, 12)
    dealer_card = cards[d]
    dealer_sum += dealer_card

    print(f"ディーラーが新しく引いたカードは、{dealer_card}　　　合計： {dealer_sum}")

    if dealer_sum > 21:
      print("Dealer Bursts！ あなたの勝ちです。")
      game_set_flag = True

if not game_set_flag:
  print(f"\nあなたの合計： {your_sum}")
  print(f"ディーラーの合計： {dealer_sum}")

  if your_sum > dealer_sum:
    print("あなたの勝ちです。")
  elif your_sum < dealer_sum:
    print("あなたの負けです。")
  else:
    print("引き分けです。")