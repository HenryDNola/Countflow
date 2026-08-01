import{r as d,q as N,j as f,R as g}from"./chunk-CKrByKvx.js";const x="div",S=d.forwardRef(({tag:e,...t},r)=>{const a=N(t)??e??x;return d.createElement(a,{...t,ref:r})});S.displayName="Text";const I=d.forwardRef(({type:e="submit",children:t,...r},a)=>f.jsx("button",{type:e,...r,ref:a,children:t}));I.displayName="Button";const R=d.forwardRef(({value:e,defaultValue:t,checked:r,defaultChecked:a,...s},i)=>{const{renderer:n}=d.useContext(g),l=n==="canvas"?String(e??t)+String(r??a):void 0;return d.createElement("input",{...s,key:l,defaultValue:e??t,defaultChecked:r??a,ref:i})});R.displayName="Input";var z=[16,32,48,64,96,128,256,384],u=[640,750,828,1080,1200,1920,2048,3840],o=[...z,...u],E=(e,t)=>{if(t){const s=/(^|\s)(1?\d?\d)vw/g,i=[];for(let n;n=s.exec(t);n)i.push(Number.parseInt(n[2],10));if(i.length){const n=Math.min(...i)*.01;return{widths:o.filter(l=>l>=u[0]*n),kind:"w"}}return{widths:o,kind:"w"}}if(e==null)return{widths:u,kind:"w"};const r=2;let a=o.findIndex(s=>s>=r*e);return a=a<0?o.length:a,{widths:o.slice(0,a+1),kind:"w"}},b=({src:e,width:t,quality:r,sizes:a,loader:s})=>{const{widths:i,kind:n}=E(t,a);return{sizes:!a&&n==="w"?"100vw":a,srcSet:i.map((l,c)=>`${s({src:e,quality:r,width:l})} ${n==="w"?l:c+1}${n}`).join(", "),src:s({src:e,quality:r,width:i[i.length-1]})}},w=e=>{if(typeof e=="number")return Math.round(e);if(typeof e=="string"){const t=Number.parseFloat(e);if(!Number.isNaN(t))return Math.round(t)}},L="(min-width: 1280px) 50vw, 100vw",k=80,M=e=>{try{return new URL(e),!0}catch{return!1}},A=e=>{const t=w(e.width),r=Math.max(Math.min(w(e.quality)??k,100),0);if(e.src!=null&&e.src!==""){if(e.src.startsWith("data:"))return{src:e.src};if(e.srcSet==null&&e.optimize){const s=e.sizes??(e.width==null?L:void 0);return b({src:e.src,width:t,quality:r,sizes:s,loader:e.loader})}const a={src:M(e.src)?e.src:e.loader({src:e.src,format:"raw"})};return e.srcSet!=null&&(a.srcSet=e.srcSet),e.sizes!=null&&(a.sizes=e.sizes),a}},v=d.forwardRef(({quality:e,loader:t,optimize:r=!0,loading:a="lazy",decoding:s="async",...i},n)=>{const l=A({src:i.src,srcSet:i.srcSet,sizes:i.sizes,width:i.width,quality:e,loader:t,optimize:r})??{src:V};return f.jsx("img",{alt:"",...i,...l,decoding:s,loading:a,ref:n})});v.displayName="Image";var V=`data:image/svg+xml;base64,${btoa(`<svg
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
</svg>`)}`;const $=d.forwardRef(({loading:e="lazy",width:t,height:r,optimize:a=!0,decoding:s,$webstudio$canvasOnly$assetId:i,...n},l)=>{const c=String(n.src??""),{imageLoader:C,renderer:y}=d.useContext(g);let h=s,m=c;return y==="canvas"&&(e="eager",h="sync",m=i??c,t!==void 0&&r!==void 0&&Number.isNaN(t)&&Number.isNaN(r)&&(a=!1,t=void 0,r=void 0)),f.jsx(v,{loading:e,decoding:h,optimize:a,width:t,height:r,...n,loader:C,src:c,ref:l},m)});$.displayName="Image";const D="ul",j="ol",T=d.forwardRef(({ordered:e=!1,...t},r)=>d.createElement(e?j:D,{...t,ref:r}));T.displayName="List";const U=d.forwardRef(({children:e,...t},r)=>f.jsx("li",{...t,ref:r,children:e}));U.displayName="ListItem";const F="hr",H=d.forwardRef((e,t)=>d.createElement(F,{...e,ref:t}));H.displayName="Separator";export{I as a,T as d,R as f,U as i,S as n,H as p,$ as y};
