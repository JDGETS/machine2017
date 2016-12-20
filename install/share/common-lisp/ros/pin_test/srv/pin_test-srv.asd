
(cl:in-package :asdf)

(defsystem "pin_test-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "LedState" :depends-on ("_package_LedState"))
    (:file "_package_LedState" :depends-on ("_package"))
  ))