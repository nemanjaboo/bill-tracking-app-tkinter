from tkinter import *
from classes import *
from calendar import monthrange
from tkinter import messagebox

click = 0


class StartScreen(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        time = datetime.datetime.now()
        today = time.strftime("%d %B %Y")
        page_date = Label(self, text='Today is {}'.format(today), font='Times 12 bold')
        page_date.place(x=1020, y=560)

        main_label = Label(self, text='Pay Your Bills', font='Whyte 35')
        main_label.pack()

        budget_label = Label(self, text='Enter your budget', font='Whyte 20')
        budget_label.place(x=830, y=60)
        budget_entry = Entry(self)
        budget_entry.place(x=870, y=100)

        desired_label = Label(self, text='Desired daily budget', font='Whyte 20')
        desired_label.place(x=830, y=130)
        desired_entry = Entry(self)
        desired_entry.place(x=870, y=170)

        calc_msg_label = Label(self, text='')
        calc_msg_label.place(x=750, y=250)

        def calculate_budget():
            """
            Function that calculates user's remaining budget depending on the entry input
            :return:
            """
            calculation_entries = [budget_entry.get(), desired_entry.get()]

            try:
                budget = float(budget_entry.get())

                cost_label = [float(bentrycost1.get()), float(bentrycost2.get()), float(bentrycost3.get()),
                              float(bentrycost4.get()),
                              float(bentrycost5.get()), float(bentrycost6.get()), float(bentrycost7.get()),
                              float(bentrycost8.get()),
                              float(bentrycost9.get()), float(bentrycost10.get())]

                remaining_budget = budget - sum(cost_label)

                daily = float(desired_entry.get())

                this_month = monthrange(datetime.datetime.now().year, datetime.datetime.now().month)
                current_day = datetime.datetime.now().day
                remaining_days = this_month[1] - current_day

                desire = daily * remaining_days

                exceeding_budget = remaining_budget - desire
                calc_msg_label.configure(
                    text='Days left:{}\nExtra budget:{}RSD'.format(remaining_days, exceeding_budget),
                    font='Whyte 18 bold')
            except:
                messagebox.showerror(title='Error', message='Make sure to input numbers')
                return

        main_button = Button(self, text='Calculate', command=calculate_budget)
        main_button.place(x=900, y=200)

        box = Frame(self)
        box.pack(anchor='w', padx=30)

        var1 = IntVar()
        var2 = IntVar()
        var3 = IntVar()
        var4 = IntVar()
        var5 = IntVar()
        var6 = IntVar()
        var7 = IntVar()
        var8 = IntVar()
        var9 = IntVar()
        var10 = IntVar()

        lf1 = LabelFrame(box, text='Bill--1', fg='black', font='Whyte')
        lf1.grid(row=0, column=0, sticky='w', pady=10)
        billname1 = Label(lf1, text='Name')
        billname1.pack()
        bentryname1 = Entry(lf1)
        bentryname1.pack()
        billcost1 = Label(lf1, text='Cost')
        billcost1.pack()
        bentrycost1 = Entry(lf1)
        bentrycost1.pack()
        chb1 = Checkbutton(lf1, text='Paid', variable=var1, onvalue=1, offvalue=0)
        chb1.pack()

        lf2 = LabelFrame(box, text='Bill--1', fg='black', font='Whyte')
        lf2.grid(row=0, column=1, sticky='w', pady=10)
        billname2 = Label(lf2, text='Name')
        billname2.pack()
        bentryname2 = Entry(lf2)
        bentryname2.pack()
        billcost2 = Label(lf2, text='Cost')
        billcost2.pack()
        bentrycost2 = Entry(lf2)
        bentrycost2.pack()
        chb2 = Checkbutton(lf2, text='Paid', variable=var2, onvalue=1, offvalue=0)
        chb2.pack()

        lf3 = LabelFrame(box, text='Bill--3', fg='black', font='Whyte')
        lf3.grid(row=0, column=2, sticky='w', pady=10)
        billname3 = Label(lf3, text='Name')
        billname3.pack()
        bentryname3 = Entry(lf3)
        bentryname3.pack()
        billcost3 = Label(lf3, text='Cost')
        billcost3.pack()
        bentrycost3 = Entry(lf3)
        bentrycost3.pack()
        chb3 = Checkbutton(lf3, text='Paid', variable=var3, onvalue=1, offvalue=0)
        chb3.pack()

        lf4 = LabelFrame(box, text='Bill--4', fg='black', font='Whyte')
        lf4.grid(row=0, column=3, sticky='w', pady=10)
        billname4 = Label(lf4, text='Name')
        billname4.pack()
        bentryname4 = Entry(lf4)
        bentryname4.pack()
        billcost4 = Label(lf4, text='Cost')
        billcost4.pack()
        bentrycost4 = Entry(lf4)
        bentrycost4.pack()
        chb4 = Checkbutton(lf4, text='Paid', variable=var4, onvalue=1, offvalue=0)
        chb4.pack()

        lf5 = LabelFrame(box, text='Bill--5', fg='black', font='Whyte')
        lf5.grid(row=0, column=4, sticky='w', pady=10)
        billname5 = Label(lf5, text='Name')
        billname5.pack()
        bentryname5 = Entry(lf5)
        bentryname5.pack()
        billcost5 = Label(lf5, text='Cost')
        billcost5.pack()
        bentrycost5 = Entry(lf5)
        bentrycost5.pack()
        chb5 = Checkbutton(lf5, text='Paid', variable=var5, onvalue=1, offvalue=0)
        chb5.pack()

        lf6 = LabelFrame(box, text='Bill--6', fg='black', font='Whyte')
        lf6.grid(row=1, column=0, sticky='w', pady=10)
        billname6 = Label(lf6, text='Name')
        billname6.pack()
        bentryname6 = Entry(lf6)
        bentryname6.pack()
        billcost6 = Label(lf6, text='Cost')
        billcost6.pack()
        bentrycost6 = Entry(lf6)
        bentrycost6.pack()
        chb6 = Checkbutton(lf6, text='Paid', variable=var6, onvalue=1, offvalue=0)
        chb6.pack()

        lf7 = LabelFrame(box, text='Bill--7', fg='black', font='Whyte')
        lf7.grid(row=1, column=1, sticky='w', pady=10)
        billname7 = Label(lf7, text='Name')
        billname7.pack()
        bentryname7 = Entry(lf7)
        bentryname7.pack()
        billcost7 = Label(lf7, text='Cost')
        billcost7.pack()
        bentrycost7 = Entry(lf7)
        bentrycost7.pack()
        chb7 = Checkbutton(lf7, text='Paid', variable=var7, onvalue=1, offvalue=0)
        chb7.pack()

        lf8 = LabelFrame(box, text='Bill--8', fg='black', font='Whyte')
        lf8.grid(row=1, column=2, sticky='w', pady=10)
        billname8 = Label(lf8, text='Name')
        billname8.pack()
        bentryname8 = Entry(lf8)
        bentryname8.pack()
        billcost8 = Label(lf8, text='Cost')
        billcost8.pack()
        bentrycost8 = Entry(lf8)
        bentrycost8.pack()
        chb8 = Checkbutton(lf8, text='Paid', variable=var8, onvalue=1, offvalue=0)
        chb8.pack()

        lf9 = LabelFrame(box, text='Bill--9', fg='black', font='Whyte')
        lf9.grid(row=1, column=3, sticky='w', pady=10)
        billname9 = Label(lf9, text='Name')
        billname9.pack()
        bentryname9 = Entry(lf9)
        bentryname9.pack()
        billcost9 = Label(lf9, text='Cost')
        billcost9.pack()
        bentrycost9 = Entry(lf9)
        bentrycost9.pack()
        chb9 = Checkbutton(lf9, text='Paid', variable=var9, onvalue=1, offvalue=0)
        chb9.pack()

        lf10 = LabelFrame(box, text='Bill--10', fg='black', font='Whyte')
        lf10.grid(row=1, column=4, sticky='w', pady=10)
        billname10 = Label(lf10, text='Name')
        billname10.pack()
        bentryname10 = Entry(lf10)
        bentryname10.pack()
        billcost10 = Label(lf10, text='Cost')
        billcost10.pack()
        bentrycost10 = Entry(lf10)
        bentrycost10.pack()
        chb10 = Checkbutton(lf10, text='Paid', variable=var10, onvalue=1, offvalue=0)
        chb10.pack()

        def submit_bills():
            """
            Function that adds users bill/s into the database and informs of any unpaid bills
            :return:
            """
            global unpaid_bills

            name_label = [bentryname1.get(), bentryname2.get(), bentryname3.get(), bentryname4.get(), bentryname5.get(),
                          bentryname6.get(), bentryname7.get(), bentryname8.get(), bentryname9.get(),
                          bentryname10.get()]

            costs = [bentrycost1.get(), bentrycost2.get(), bentrycost3.get(), bentrycost4.get(), bentrycost5.get(),
                     bentrycost6.get(), bentrycost7.get(), bentrycost8.get(), bentrycost9.get(), bentrycost10.get()]

            cost_label = []

            for cost in costs:
                try:
                    if cost != '':
                        cost_label.append(float(int(cost)))
                except ValueError:
                    messagebox.showinfo(title='Info', message='Cost must be entered in numbers')
                    return

            entries = [bentryname1, bentryname2, bentryname3, bentryname4, bentryname5, bentryname6,
                       bentryname7, bentryname8, bentryname9, bentryname10, bentrycost1, bentrycost2, bentrycost3,
                       bentrycost4, bentrycost5, bentrycost6, bentrycost7, bentrycost8, bentrycost9, bentrycost10]

            checkbuttons = [var1.get(), var2.get(), var3.get(), var4.get(), var5.get(), var6.get(), var7.get(),
                            var8.get(), var9.get(), var10.get()]

            all_bills = []

            for n in range(len(name_label)):
                if name_label[n] != '' and cost_label[n] != '':
                    all_bills.append([name_label[n], cost_label[n], checkbuttons[n]])
            for i in range(len(all_bills)):
                if all_bills[i][2] == 0:
                    all_bills[i][2] = 'Not Paid'
                else:
                    all_bills[i][2] = 'Paid'


            for i in range(len(all_bills)):
                new_bill = Bill(Bill.get_month(), all_bills[i][0], all_bills[i][1], all_bills[i][2])
                insert_bill_to_table(new_bill)

            unpaid_bills = 0
            for bill in all_bills:
                if bill[2] == 'Not Paid':
                    unpaid_bills += 1

            total_cost = 0.0
            for i in range(len(all_bills)):
                if all_bills[i][2] == 'Paid':
                    total_cost += all_bills[i][1]

            costlabel.configure(text='Total paid:' + ' ' + str(total_cost) + 'RSD')
            notpaid_label.configure(text='Unpaid bills:' + str(unpaid_bills))

            messagebox.showinfo(title='Info', message='Bills are in database.')

            for entry in entries:
                entry.delete(0, 'end')

        main_button = Button(box, text='SUBMIT ALL', command=lambda: submit_bills())
        main_button.grid(row=2, column=2)

        def clear_all():
            """
            Function for clearing all bill entries
            """
            entries = [bentryname1, bentryname2, bentryname3, bentryname4, bentryname5, bentryname6,
                       bentryname7, bentryname8, bentryname9, bentryname10, bentrycost1, bentrycost2, bentrycost3,
                       bentrycost4, bentrycost5, bentrycost6, bentrycost7, bentrycost8, bentrycost9, bentrycost10]
            for entry in entries:
                entry.delete(0, 'end')

        clear_button = Button(box, text='Clear all', command=clear_all)
        clear_button.grid(row=2, column=4)

        costlabel = Label(self, fg='black', font='Whyte 18 bold')
        costlabel.place(x=100, y=400)
        notpaid_label = Label(self, fg='black', font='Whyte 18 bold')
        notpaid_label.place(x=100, y=450)


class Sorting(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        main_label = Label(self, text='Find your bills', font='Whyte 15')
        main_label.pack()

        pick_frame = Frame(self, )
        pick_frame.pack(side=TOP, anchor='n', padx=10, pady=20)
        results_frame = Frame(self, )
        results_frame.pack(side=TOP, anchor='s')
        options = ['By name', 'By month', 'By year', 'Not Paid', 'Total Not Paid', 'Total Paid']
        # RESULTS_FRAME#

        results_label = Label(results_frame)
        results_label.grid(row=0, column=0)

        # PICK_FRAME#
        namesset = set()
        prenames = get_bill_names()
        for name in prenames:
            namesset.add(name)
        names = []
        for i in namesset:
            names.append(i)
        names.sort(reverse=True)
        full_date = get_bill_dates()
        months = set()
        years = set()
        for i in full_date:
            months.add(i[0][0:-5])
            years.add(i[0][-4:])

        paid = get_paid_bills()
        not_paid = get_not_paid_bills()

        lb1 = Listbox(pick_frame, height=6)
        for i in range(len(options)):
            lb1.insert(i, options[i])
        lb1.grid(row=0, column=0)

        lb2 = Listbox(pick_frame, height=6)
        lb2.grid(row=2, column=0)

        def get_back(info):
            """
            Button function for browsing back through found results
            :param info: found results
            """
            global click
            click -= 1
            try:
                results_label.configure(font='Whyte 12 bold',
                                        text='{}---{}---{}---{}'.format(info[click][0], info[click][1], info[click][2],
                                                                        info[click][3]), )
            except IndexError:
                click = 0
                results_label.configure(font='Whyte 12 bold',
                                        text='{}---{}---{}---{}'.format(info[click][0], info[click][1], info[click][2],
                                                                        info[click][3]))

        def get_next(info):
            """
            Button function for browsing next through found results
            :param info: found results
            """
            global click
            try:
                results_label.configure(
                    text='{}---{}---{}---{}'.format(info[click][0], info[click][1], info[click][2], info[click][3]))
                click += 1
            except IndexError:
                click = 0
                results_label.configure(
                    text='{}---{}---{}---{}'.format(info[click][0], info[click][1], info[click][2], info[click][3]))

        def find_name():
            """
            Function that gets and shows the results from the search by name
            :return: list of the results
            """
            name = lb2.curselection()
            selected = ''
            for n in name:
                selected += lb2.get(n)[0]
            found = get_bill_by_name(selected)
            results_label.configure(font='Whyte 12 bold',
                                    text='{}---{}---{}---{}'.format(found[0][0], found[0][1], found[0][2], found[0][3]))
            b1 = Button(results_frame, text='Back', command=lambda: get_back(find_name()))
            b1.grid(row=1, column=0)
            b2 = Button(results_frame, text='Next', command=lambda: get_next(find_name()))
            b2.grid(row=2, column=0)
            return found

        def find_month():
            """
            Function that gets and shows the results from the search by month
            :return: list of the results
            """
            name = lb2.curselection()
            selected = ''
            for n in name:
                selected += lb2.get(n)
            found = get_bill_by_month(selected)
            results_label.configure(font='Whyte 12 bold',
                                    text='{}---{}---{}---{}'.format(found[0][0], found[0][1], found[0][2], found[0][3]))
            b1 = Button(results_frame, text='Back', command=lambda: get_back(find_month()))
            b1.grid(row=1, column=0)
            b2 = Button(results_frame, text='Next', command=lambda: get_next(find_month()))
            b2.grid(row=2, column=0)
            return found

        def find_year():
            """
            Function that gets and shows the results from the search by year
            :return: list of the results
            """
            name = lb2.curselection()
            selected = ''
            for n in name:
                selected += lb2.get(n)
            found = get_bill_by_year(selected)
            b1 = Button(results_frame, text='Back', command=lambda: get_back(find_year()))
            b1.grid(row=1, column=0)
            b2 = Button(results_frame, text='Next', command=lambda: get_next(find_year()))
            b2.grid(row=2, column=0)
            return found

        def get_selection():
            """
            Function for filling the listbox with the search terms or displaying the immediate results
            """
            select = lb1.curselection()
            user_select = options[select[0]]
            lb2.delete(0, END)
            if user_select == 'By name':
                for i in names:
                    lb2.insert(0, i)
                    b = Button(pick_frame, text='Get', command=lambda: find_name())
                    b.grid(row=3, column=0)
            if user_select == 'By month':
                for i in months:
                    lb2.insert(12, i)
                b = Button(pick_frame, text='Get', command=lambda: find_month())
                b.grid(row=3, column=0)
            if user_select == 'By year':
                for i in years:
                    lb2.insert(12, i)
                b = Button(pick_frame, text='Get', command=lambda: find_year())
                b.grid(row=3, column=0)
            if user_select == 'Not Paid':
                found = get_not_paid_bills()
                results_label.configure(font='Whyte 12 bold',
                                        text='{}---{}---{}---{}'.format(found[0][0], found[0][1], found[0][2],
                                                                        found[0][3]))
                b1 = Button(results_frame, text='Back', command=lambda: get_back(found))
                b1.grid(row=1, column=0)
                b2 = Button(results_frame, text='Next', command=lambda: get_next(found))
                b2.grid(row=2, column=0)
            if user_select == 'Total Not Paid':
                total = 0
                for i in range(len(not_paid)):
                    total += not_paid[i][2]
                results_label.configure(font='Whyte 12 bold', text='Total not paid:{:.2f}RSD'.format(total))
            if user_select == 'Total Paid':
                total = 0
                for i in range(len(paid)):
                    total += paid[i][2]
                results_label.configure(font='Whyte 12 bold', text='Total paid:{:.2f}RSD'.format(total))

        b1 = Button(pick_frame, text='Find', command=lambda: get_selection())
        b1.grid(row=1, column=0)


class EditPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        main_label = Label(self, text='Find your bills', font='Whyte 15')
        main_label.pack()

        edit_label = Label(self, text='Select a bill you want to edit')
        edit_label.pack()

        all_bills = get_not_paid_bills()
        all_bills.sort(key=lambda x: x[1][0].upper())
        lb1 = Listbox(self, width=37)
        for i in range(len(all_bills)):
            lb1.insert(i,
                       all_bills[i][0] + '--' + all_bills[i][1] + '--' + str(all_bills[i][2]) + '--' + all_bills[i][3])
        lb1.pack()

        def get_select():
            """
            Function for selecting the desired bill from the listbox
            """
            s = lb1.curselection()
            user_select = all_bills[s[0]]
            wanted_bill = get_exact_bill(user_select[0], user_select[1], user_select[2], user_select[3])
            bill_label.configure(font='Whyte 12 bold',
                                 text='Selected:\n{}--{}--{}--{}'.format(user_select[0], user_select[1], user_select[2],
                                                                         user_select[3]))

        def update_status():
            """
            Function for changing the status of the selected bill
            """
            s = lb1.curselection()
            user_select = all_bills[s[0]]
            decision = messagebox.askyesno(title='Update',
                                           message='Change to paid\n{}-{}-{}-{}'.format(user_select[0], user_select[1],
                                                                                        user_select[2], user_select[3]))
            if decision:
                update_bill(user_select[0], user_select[1], user_select[2], user_select[3])
                all_bills1 = get_not_paid_bills()
                lb1.delete(0, END)
                for i in range(len(all_bills1)):
                    lb1.insert(i,
                               all_bills1[i][0] + '--' + all_bills1[i][1] + '--' + str(all_bills1[i][2]) + '--' +
                               all_bills1[i][3])
                    lb1.pack()
                update_label.configure(text='Bill updated!', font='Whyte 15 bold')
                bill_label.configure(text='')
            else:
                pass

        b1 = Button(self, text='Select', command=lambda: get_select())
        b1.pack()

        bill_label = Label(self)
        bill_label.pack()

        b2 = Button(self, text='Change to Paid', command=lambda: update_status())
        b2.pack()

        update_label = Label(self)
        update_label.pack()
