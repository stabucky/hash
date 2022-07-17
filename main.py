import streamlit as st
import hashlib

def main():
  st.title("Hash")
  with st.form("my_form"):
    textarea_val=st.text_area("Texts",value="",placeholder="ここに文字列をセット。")
    submitted = st.form_submit_button("Submit")
  if submitted:
    if not textarea_val == "":
      result=make_hash(textarea_val)
  st.write("&copy;2022You Look Too Cool")

def make_hash(text):
  names = sorted(hashlib.algorithms_guaranteed)
  lines=[]
  for name in names:
    temp = "hashlib." + name + "(text.encode()).hexdigest()"
    try:
      hs = eval(temp)
    except TypeError:
      continue
    st.text(name)
    st.code(hs)

if __name__ == "__main__":
  main()
