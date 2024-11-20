import tkinter as tk
from tkinter import messagebox
from mm_recipes import MMRecipeManager


def main():

    app=tk.Tk()
    app.title("MM egeszseges receptek")
    app.geometry("720x512")
    
    manager=MMRecipeManager("recipes.json")
    tk.Label(app, text="Adj meg egy alapanyagot: ").pack(pady=10)
    ingredient_entry=tk.Entry(app, width=40)
    ingredient_entry.pack()

    def search_recipes():
        ingredient=ingredient_entry.get();
        if not ingredient:
            messagebox.showerror("Hiba", "Adj meg egy alapanyagot!")
            return
        results=manager.search_recipes_by_ingredient(ingredient)

        if results:
            messagebox.showinfo("Talalatok","\n".join(results))
        else:
            messagebox.showinfo("Talalatok","Nincs recept mely tartalmazza a megadott alapanyagot.")

    tk.Button(app, text="Receptek keresese", command=search_recipes).pack(pady=10)

    app.mainloop()

if __name__=="__main__":
    main()
