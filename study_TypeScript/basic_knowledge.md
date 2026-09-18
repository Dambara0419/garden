## Type anotation
primitive typeの指定
let v_bool: boolean = true;
let v_null: null = null;
let v_undef: undefined = undefined;
let v_num: number = 123;
let v_bigint: bigint = 11451481093189319194545072136436489464n;
let v_str: string = "Hello, world!";

## array and object
let coffees: string[] = ['French Roast', 'Colombian', 'Kona'];
var car: object = { myCar: 'Saturn', getCar: 'Honda', special: 'Toyota' };

## 共同型
|を使うことで２つ以上の型を指定できる
var answer: number | string = 42;
answer = 'Thanks for all the fish...';
それかany使えばプリミティブを含む任意の型を許容
var answer: any = 42;
answer = 'Thanks for all the fish...';

数値と文字列を+演算子で結合する式では、TypeScriptは数値を文字列に変換します
var x = '答えは ' + 42; // "答えは 42"
var y = 42 + ' が答え'; // "42 が答え"
> なんでこれだけ？暗黙の型変換許す？？

if文などの制御フローやtry...catch構文はJavaScriptと同じ
ループ文はJavaScriptと同じ
式と演算子はJavaScriptと同じ
テキスト処理はJavaScriptと同じ
正規表現はJavaScriptと同じ

### interface 型
interface は、TypeScript で「オブジェクトの形」に名前を付けて宣言するためのキーワードです。

書き方

interface Props {        // interface 型の名前 {
  title?: string         //   キー名: 型
  description?: string   //   キー名?: 型（? は省略可能）
}                        // }

- Props の部分は自由に付けられる名前です。ただし Astro では、Props という名前のときだけ Astro.props の型として自動で使われます。
- 型名は大文字で始めるのが慣習です。

JavaScript には存在しない
interface は TypeScript だけの文法です。.js ファイルに書くと文法エラーになります。前に話したとおり、型チェックが終わると消えるので、実行されるコードには残りません。
