// 用假 DOM 跑页面顶层脚本，抓 ReferenceError 这类"删了声明忘了引用"的问题。
// 用法: node smoke_page.js <inline.js>
const fs = require("fs");
const raw = fs.readFileSync(process.argv[2], "utf8");
// 金版模板里的占位符：serve 时才注入，冒烟里给个空值
const src = raw.replace(/__MODULES_DEFAULT__/g, '""').replace(/__CONSOLE_TOKEN__/g, "");

function fakeEl() {
  const el = {
    classList: { add() {}, remove() {}, toggle() {}, contains() { return false; } },
    style: {},
    dataset: {},
    files: [],
    options: [],
    children: [],
    value: "",
    textContent: "",
    innerHTML: "",
    hidden: false,
    checked: false,
    disabled: false,
    href: "",
    title: "",
    addEventListener() {},
    removeEventListener() {},
    appendChild() {},
    removeChild() {},
    setAttribute() {},
    getAttribute() { return ""; },
    removeAttribute() {},
    remove() {},
    focus() {},
    click() {},
    dispatchEvent() {},
    querySelector() { return fakeEl(); },
    querySelectorAll() { return []; },
    closest() { return null; },
    matches() { return false; },
    insertAdjacentHTML() {},
  };
  return el;
}

global.document = {
  getElementById() { return fakeEl(); },
  querySelector() { return fakeEl(); },
  querySelectorAll() { return []; },
  createElement() { return fakeEl(); },
  addEventListener() {},
  body: fakeEl(),
  documentElement: fakeEl(),
  head: fakeEl(),
};
global.window = global;
global.addEventListener = () => {};
global.removeEventListener = () => {};
global.localStorage = { getItem() { return null; }, setItem() {}, removeItem() {} };
global.sessionStorage = { getItem() { return null; }, setItem() {}, removeItem() {} };
global.navigator = { userAgent: "smoke", clipboard: { writeText() { return Promise.resolve(); } } };
global.location = {
  href: "file:///smoke.html", search: "", protocol: "file:", port: "", hash: "",
  reload() {}, assign() {}, replace() {},
};
global.fetch = () => Promise.reject(new Error("smoke: no network"));
global.alert = () => {};
global.confirm = () => false;
global.setTimeout = (fn) => 0;
global.setInterval = () => 0;
global.requestAnimationFrame = () => 0;

try {
  new Function(src)();
  console.log("SMOKE OK: 顶层脚本执行未抛错");
} catch (e) {
  console.log("SMOKE FAIL:", e && e.message);
  process.exit(1);
}
