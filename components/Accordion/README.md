見出しを押して、中身を開いたり閉じたりする一覧。よくある質問、設定のまとまり、長い説明の折りたたみに使う。
*Headings that expand and collapse their content: FAQs, settings groups, long explanations.*

## 使い方 / Usage
- 見出しは中身を言い当てる名詞句にする（「通知」「アカウント」）。右側に `meta` で要約（「オン・3 件」）を出せる。
  *Headings are noun phrases; `meta` shows a short summary on the right.*
- 既定では複数を同時に開ける。1 つだけにしたいときは `multiple={false}`。最初に開いておくものは `defaultOpen`。
  *Several can be open by default; `multiple={false}` allows only one; `defaultOpen` sets the initial state.*
- 大事な情報や、ほとんどの人が読む内容は畳まない。畳むのは「読まない人が多いもの」だけ。
  *Never collapse important or commonly read content.*
- 見出しは本物の見出し（既定は h3、`headingLevel` で変える）の中のボタンで、`aria-expanded` で開閉が伝わる（W3C APG の Accordion）。
  *Each heading is a real heading containing a button with `aria-expanded` (W3C APG Accordion).*

## 利用側が渡すもの / You provide
`items`（`{value, title, content, meta?}`）、必要なら `multiple`・`defaultOpen`・`headingLevel`・`onChange`。

**理由 / Why:** 長い内容を必要な分だけ読む。見出しだけ並べ、開いたところだけ読む。
*Long content read only as needed: show headings, read what you open.*
