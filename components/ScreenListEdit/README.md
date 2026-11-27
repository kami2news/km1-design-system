一覧・詳細・編集の組み合わせの例: 左の一覧で選び、右でその場の編集（ExpansionEditor）、まとめて削除は確認（Dialog）と「元に戻す」（Toast）。
*A screen pattern combining several components; also used for the scenario checks in README.*

**理由 / Why:** 一覧から選んだ人が知りたいのはその授業の中身なので、右側は名前を大きく上に出し、教室と時限は「登録内容」のまとまりに 1 回だけ並べる（名前の下に同じ値を要約として重ねると、同じことを 2 回読ませる無駄になる）。直せない項目も同じ並びに置き、直せない理由をすぐ下に書く。
*People who pick a course want its contents, so the right side leads with its name, and room and period appear once, in the details group (repeating them as a summary makes people read the same thing twice); read-only items share the row layout with the reason beneath.*

**狭い画面 / Narrow screens:** 640px 未満では一覧と詳細を別の画面にする。一覧から始め、行を押すと詳細だけになり、「授業の一覧に戻る」で一覧に戻って、開いていた行にフォーカスを返す（「画面の組み立て」の一覧・詳細、D40）。
*Below 640px list and detail are separate screens; back returns focus to the row that was open.*
