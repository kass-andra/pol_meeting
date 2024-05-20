import streamlit as st
import pandas as pd


dates = ["24 мая (пт)", "25 мая (сб)", "26 мая (вс)", "27 мая (пн)", "28 мая (вт)", 
         "29 мая (ср)", "30 мая (чт)", "31 мая (пт)", "01 июня (сб)", "02 июня (вс)",
         "03 июня (пн)", "04 июня (вт)", "05 июня (ср)", "06 июня (чт)", "07 июня (пт)", 
         "08 июня (сб)", "09 июня (вс)"]
times = ["10-12", "12-14", "14-16", "16-18", "18-20", "20-22", "22-24"]

columns = pd.MultiIndex.from_product([dates, times])
columns_sum = ['\n'.join(col) for col in product(dates, times)]

# Создаем пустой DataFrame с мультииндексом колонок для данных
df = pd.DataFrame(columns=columns)

# Создаем пустой DataFrame с мультииндексом колонок для сумм
sums_df = pd.DataFrame(0, index=['Сумма'], columns=columns_sum)

# # Функция для отображения чекбоксов и обновления таблицы
# def update_schedule(df, sums_df):
#     st.title("Расписание собраний")
#     st.write("Выберите удобные временные интервалы:")

#     with st.form(key='schedule_form'):
#         selected_times = {}
#         for date in dates:
#              st.write(f"{date}")
#              cols = st.columns(len(times))
#              for i, time in enumerate(times):
#                  col_key = (date, time)
#                  selected_times[col_key] = cols[i].checkbox(time, key=f"{date}-{time}")
        
#         submitted = st.form_submit_button("Отправить")

#     if submitted:
#         new_row = []
#         for col in df.columns:
#             new_row.append(1 if selected_times[col] else 0)
        
#         # Добавляем новую строку в DataFrame данных
#         df.loc[len(df)] = new_row

#         # Обновляем суммы в DataFrame сумм
#         sums_df.loc['Сумма'] = df.sum(axis=0)
        
#         st.success("Ваши данные были успешно обновлены!")
        
#     return df, sums_df


# Функция для отображения чекбоксов и обновления таблицы
def update_schedule(df, sums_df):
    st.title("Расписание собраний")
    st.write("Выберите удобные временные интервалы:")

    with st.form(key='schedule_form'):
        selected_times = {}

        # Отображение чекбоксов в виде таблицы
        st.write("<style>div.row-widget.stRadio>div{flex-direction:row;}</style>", unsafe_allow_html=True)
        st.write("<style>.main_container{display: flex; flex-direction: row;}</style>", unsafe_allow_html=True)
        st.write("<style>.widgetrow{display: flex; flex-direction: row;}</style>", unsafe_allow_html=True)
        st.write("<style>.widgetcol{display: flex; flex-direction: column;}</style>", unsafe_allow_html=True)

        st.write("<div class='main_container'>", unsafe_allow_html=True)
        st.write("<div class='widgetcol'>", unsafe_allow_html=True)

        # Заголовки столбцов
        st.write("<div class='widgetrow'>", unsafe_allow_html=True)
        st.write("<div class='widgetcol'></div>", unsafe_allow_html=True)
        for time in times:
            st.write(f"<div class='widgetcol'>{time}</div>", unsafe_allow_html=True)
        st.write("</div>", unsafe_allow_html=True)

        for date in dates:
            # Дата в качестве заголовка строки
            st.write("<div class='widgetrow'>", unsafe_allow_html=True)
            st.write(f"<div class='widgetcol'>{date}</div>", unsafe_allow_html=True)
            
            # Чекбоксы для временных интервалов
            for time in times:
                col_key = (date, time)
                selected_times[col_key] = st.checkbox('', key=f'{date}-{time}')
                st.write(f"<div class='widgetcol'>{selected_times[col_key]}</div>", unsafe_allow_html=True)
            
            st.write("</div>", unsafe_allow_html=True)

        st.write("</div>", unsafe_allow_html=True)
        st.write("</div>", unsafe_allow_html=True)

        submitted = st.form_submit_button("Отправить")

    if submitted:
        new_row = []
        for col in df.columns:
            new_row.append(1 if selected_times[col] else 0)
        
        # Добавляем новую строку в DataFrame данных
        df.loc[len(df)] = new_row

        # Обновляем суммы в DataFrame сумм
        sums_df.loc['Сумма'] = df.sum(axis=0)
        
        st.success("Ваши данные были успешно обновлены!")
        
    return df, sums_df


# # Отображение текущего состояния таблицы данных
# st.write("Текущее состояние таблицы:")
# st.write(df)

# Обновление расписания
df, sums_df = update_schedule(df, sums_df)

# Сохранение данных в сессии Streamlit
st.session_state.df = df
st.session_state.sums_df = sums_df

# # Применение CSS для поворота заголовков
# st.markdown("""
#     <style>
#     .css-1d391kg {
#         transform: rotate(90deg);
#         white-space: nowrap;
#         height: 200px;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # Отображение таблицы с повернутыми заголовками
# st.write(sums_df.style.set_table_styles({
#     ('24 мая (пт)', '16-18'): [
#         {'selector': 'th', 'props': 'transform: rotate(90deg); white-space: nowrap; height: 200px;'}
#     ],
#     ('24 мая (пт)', '18-20'): [
#         {'selector': 'th', 'props': 'transform: rotate(90deg); white-space: nowrap; height: 200px;'}
#     ],
#     ('24 мая (пт)', '20-22'): [
#         {'selector': 'th', 'props': 'transform: rotate(90deg); white-space: nowrap; height: 200px;'}
#     ],
# }
#                                   ))

# Отображение сумм по каждому столбцу
st.write("Сумма по каждому столбцу:")
st.write(sums_df)
