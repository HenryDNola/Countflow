import{r as d,j as o,R as g}from"./chunk-D5DiX7_-.js";const N=d.forwardRef(({type:e="submit",children:t,...r},i)=>o.jsx("button",{type:e,...r,ref:i,children:t}));N.displayName="Button";const x=d.forwardRef(({value:e,defaultValue:t,checked:r,defaultChecked:i,...s},a)=>{const{renderer:n}=d.useContext(g),l=n==="canvas"?String(e??t)+String(r??i):void 0;return d.createElement("input",{...s,key:l,defaultValue:e??t,defaultChecked:r??i,ref:a})});x.displayName="Input";var S=[16,32,48,64,96,128,256,384],f=[640,750,828,1080,1200,1920,2048,3840],u=[...S,...f],I=(e,t)=>{if(t){const s=/(^|\s)(1?\d?\d)vw/g,a=[];for(let n;n=s.exec(t);n)a.push(Number.parseInt(n[2],10));if(a.length){const n=Math.min(...a)*.01;return{widths:u.filter(l=>l>=f[0]*n),kind:"w"}}return{widths:u,kind:"w"}}if(e==null)return{widths:f,kind:"w"};const r=2;let i=u.findIndex(s=>s>=r*e);return i=i<0?u.length:i,{widths:u.slice(0,i+1),kind:"w"}},z=({src:e,width:t,quality:r,sizes:i,loader:s})=>{const{widths:a,kind:n}=I(t,i);return{sizes:!i&&n==="w"?"100vw":i,srcSet:a.map((l,c)=>`${s({src:e,quality:r,width:l})} ${n==="w"?l:c+1}${n}`).join(", "),src:s({src:e,quality:r,width:a[a.length-1]})}},w=e=>{if(typeof e=="number")return Math.round(e);if(typeof e=="string"){const t=Number.parseFloat(e);if(!Number.isNaN(t))return Math.round(t)}},R="(min-width: 1280px) 50vw, 100vw",b=80,E=e=>{try{return new URL(e),!0}catch{return!1}},L=e=>{const t=w(e.width),r=Math.max(Math.min(w(e.quality)??b,100),0);if(e.src!=null&&e.src!==""){if(e.src.startsWith("data:"))return{src:e.src};if(e.srcSet==null&&e.optimize){const s=e.sizes??(e.width==null?R:void 0);return z({src:e.src,width:t,quality:r,sizes:s,loader:e.loader})}const i={src:E(e.src)?e.src:e.loader({src:e.src,format:"raw"})};return e.srcSet!=null&&(i.srcSet=e.srcSet),e.sizes!=null&&(i.sizes=e.sizes),i}},v=d.forwardRef(({quality:e,loader:t,optimize:r=!0,loading:i="lazy",decoding:s="async",...a},n)=>{const l=L({src:a.src,srcSet:a.srcSet,sizes:a.sizes,width:a.width,quality:e,loader:t,optimize:r})??{src:k};return o.jsx("img",{alt:"",...a,...l,decoding:s,loading:i,ref:n})});v.displayName="Image";var k=`data:image/svg+xml;base64,${btoa(`<svg
  width="140"
  height="140"
  viewBox="0 0 600 600"
  fill="none"
  xmlns="http://www.w3.org/2000/svg"
  >
  <rect width="600" height="600" fill="#DFE3E6" />
  <path
    fill-rule="evenodd"
    clip-rule="evenodd"
    d="M450 170H150C141.716 170 135 176.716 135 185V415C135 423.284 141.716 430 150 430H450C458.284 430 465 423.284 465 415V185C465 176.716 458.284 170 450 170ZM150 145C127.909 145 110 162.909 110 185V415C110 437.091 127.909 455 150 455H450C472.091 455 490 437.091 490 415V185C490 162.909 472.091 145 450 145H150Z"
    fill="#C1C8CD"
  />
  <path
    d="M237.135 235.012C237.135 255.723 220.345 272.512 199.635 272.512C178.924 272.512 162.135 255.723 162.135 235.012C162.135 214.301 178.924 197.512 199.635 197.512C220.345 197.512 237.135 214.301 237.135 235.012Z"
    fill="#C1C8CD"
  />
  <path
    d="M160 405V367.205L221.609 306.364L256.552 338.628L358.161 234L440 316.043V405H160Z"
    fill="#C1C8CD"
  />
</svg>`)}`;const M=d.forwardRef(({loading:e="lazy",width:t,height:r,optimize:i=!0,decoding:s,$webstudio$canvasOnly$assetId:a,...n},l)=>{const c=String(n.src??""),{imageLoader:C,renderer:y}=d.useContext(g);let h=s,m=c;return y==="canvas"&&(e="eager",h="sync",m=a??c,t!==void 0&&r!==void 0&&Number.isNaN(t)&&Number.isNaN(r)&&(i=!1,t=void 0,r=void 0)),o.jsx(v,{loading:e,decoding:h,optimize:i,width:t,height:r,...n,loader:C,src:c,ref:l},m)});M.displayName="Image";const A="ul",V="ol",D=d.forwardRef(({ordered:e=!1,...t},r)=>d.createElement(e?V:A,{...t,ref:r}));D.displayName="List";const $=d.forwardRef(({children:e,...t},r)=>o.jsx("li",{...t,ref:r,children:e}));$.displayName="ListItem";const j="hr",U=d.forwardRef((e,t)=>d.createElement(j,{...e,ref:t}));U.displayName="Separator";export{D as d,x as f,$ as i,N as n,U as p,M as y};
