import { CommonModule } from '@angular/common';
import { Component, effect, ElementRef, input, signal, untracked, viewChild } from '@angular/core';

@Component({
  selector: 'app-input-box',
  imports: [CommonModule],
  template: `    
    <div class="grid grid-cols-[auto_1fr] w-full items-center gap-1 bg-mono-1 
    has-valid:!bg-hue-4 has-focus:bg-hue-2 has-invalid:!bg-hue-5 group 
    text-base rounded-lg m-1 p-[1px] transition relative mb-6">
        <div class="contents *:px-2 *:py-1"> 
            <ng-content select="label"></ng-content>
        </div>
        <div class="contents *:text-mono-1 *:bg-base *:h-full *:w-full *:border-0 
        *:rounded-l-none *:rounded-r-lg *:focus:outline-0 *:rounded-lg *:px-2 *:py-1 "         
        #inputContainer>
            <ng-content select="input"></ng-content>
        </div>
        <div class="absolute -bottom-5 left-0 text-hue-5 text-xs px-2 py-1 transition opacity-0 -z-10 -translate-y-5 group-has-invalid:translate-y-0 group-has-invalid:opacity-100 ">
            {{errorMessage()}}
        </div>
    </div>
  `,
  styles:``
})
export class InputBoxComponent {
    error = input.required<string>();

    inputContainerRef = viewChild<ElementRef>("inputContainer");
    inputElement?:HTMLInputElement;

    errorMessage = signal("")

    constructor(){
        effect(()=>{
            this.error();
            this.refreshErrorMessage();
        })
    }

    refreshErrorMessage(){
        this.inputElement?.setCustomValidity("");
        const msg = this.inputElement?.validationMessage;
        if(!msg){
            this.inputElement?.setCustomValidity(untracked(()=>this.error()));
        }
        this.errorMessage.set(this.inputElement?.validationMessage||'');
    }

    ngOnInit(){
        this.inputElement = this.inputContainerRef()?.nativeElement.querySelector("input");
        this.inputElement?.addEventListener('input',()=>this.refreshErrorMessage())
    }
}
